\c postgres;
DROP DATABASE IF EXISTS web_scraper;

CREATE DATABASE web_scraper;
\c web_scraper;

CREATE TABLE websites (
    id SERIAL PRIMARY KEY,
    domain TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pages (
    id SERIAL PRIMARY KEY,
    website_id INT NOT NULL REFERENCES websites(id) ON DELETE CASCADE,
    url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (website_id, url)
);

CREATE TABLE page_visits (
    id SERIAL PRIMARY KEY,
    page_id INT NOT NULL REFERENCES pages(id) ON DELETE CASCADE,
    visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    page_title TEXT,
    meta_description TEXT,
    meta_keywords TEXT
);

CREATE TABLE scraped_elements (
    id SERIAL PRIMARY KEY,
    page_visit_id INT NOT NULL REFERENCES page_visits(id) ON DELETE CASCADE,
    tag_name TEXT NOT NULL,
    content TEXT NOT NULL,
    attributes JSONB,
    content_hash TEXT NOT NULL,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rendered_text TEXT
);
