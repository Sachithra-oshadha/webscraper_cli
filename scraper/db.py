import psycopg2
from psycopg2.extras import Json
import hashlib
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class DatabaseLogger:
    def __init__(self, dsn):
        self.conn = psycopg2.connect(dsn)
        self.conn.autocommit = True

    def _get_site_domain(self, url):
        parsed = urlparse(url)
        return parsed.netloc

    def log_page_visit(self, url, html):
        """
        Log a new page visit to the database.
        Deduplicates elements using content_hash and stores rendered text.
        """
        soup = BeautifulSoup(html, "lxml")
        domain = self._get_site_domain(url)

        with self.conn.cursor() as cur:
            # Insert or get website
            cur.execute("""
                INSERT INTO websites (domain)
                VALUES (%s)
                ON CONFLICT (domain) DO UPDATE SET domain = EXCLUDED.domain
                RETURNING id;
            """, (domain,))
            website_id = cur.fetchone()[0]

            # Insert or get page
            cur.execute("""
                INSERT INTO pages (website_id, url)
                VALUES (%s, %s)
                ON CONFLICT (website_id, url) DO UPDATE SET url = EXCLUDED.url
                RETURNING id;
            """, (website_id, url))
            page_id = cur.fetchone()[0]

            # Extract metadata
            title = soup.title.string if soup.title else None
            meta_desc_tag = soup.find("meta", attrs={"name": "description"})
            meta_desc = meta_desc_tag["content"] if meta_desc_tag else None
            meta_keys_tag = soup.find("meta", attrs={"name": "keywords"})
            meta_keys = meta_keys_tag["content"] if meta_keys_tag else None

            # Insert page visit
            cur.execute("""
                INSERT INTO page_visits (page_id, page_title, meta_description, meta_keywords)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
            """, (page_id, title, meta_desc, meta_keys))
            page_visit_id = cur.fetchone()[0]

            # Insert scraped elements
            for tag in soup.find_all(True):
                raw_html = str(tag)
                rendered_text = tag.get_text(strip=True)  # New: rendered text only
                tag_name = tag.name
                attributes = dict(tag.attrs)

                content_hash = hashlib.sha256(raw_html.encode()).hexdigest()

                # Check if this content_hash already exists for this page
                cur.execute("""
                    SELECT id FROM scraped_elements
                    WHERE page_visit_id = %s AND content_hash = %s;
                """, (page_visit_id, content_hash))

                if cur.fetchone():
                    # Duplicate element, skip
                    continue

                cur.execute("""
                    INSERT INTO scraped_elements
                    (page_visit_id, tag_name, content, rendered_text, attributes, content_hash)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, (
                    page_visit_id,
                    tag_name,
                    raw_html,
                    rendered_text,       # Store rendered text
                    Json(attributes),
                    content_hash
                ))
