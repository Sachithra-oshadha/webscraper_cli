# Web Scraper CLI

An interactive command-line web scraper that uses a real browser engine to navigate websites, interact with elements, and persist scraped data into a PostgreSQL database.

Unlike basic scrapers, this tool supports JavaScript-rendered pages, simulates real user interactions, and tracks changes over time across multiple websites and page visits.

---

## Features

### Browser & CLI

- Navigate to any website
- Display page title and HTML source
- Capture HTML sections using CSS selectors
- Click elements programmatically
- Maintain navigation history (back/forward)
- Command-based, extensible CLI architecture
- Headless browser automation using Playwright

### Data Persistence (PostgreSQL)
- Multi-website support
- Page-level visit tracking with timestamps
- Element-level scraping by HTML tag
- Deduplication using content hashing
- Store only changed elements per visit
- Store both raw HTML and rendered text
- JSONB storage for HTML attributes

### Deployment
- Python virtual environment support
- Fully containerized with Docker
- Headless-safe execution (CI / servers / Docker)

---
## Architecture Overview
```
CLI → Playwright Browser → Navigator
                     ↓
                Database Logger
                     ↓
                PostgreSQL
```
Each page navigation:
- Creates a new page visit
- Extracts all HTML elements
- Deduplicates content using SHA-256 hashes
- Stores only new/changed elements

## Prerequisites (Local)

- Python **3.13 or higher**
- pip (Python package manager)
- PostgreSQL (local or Docker)

---

## Setup Using a Virtual Environment

### 1. Clone the repository

```bash
git clone https://github.com/Sachithra-oshadha/webscraper_cli.git
cd webscraper_cli
```

### 2. Create a virtual environment
On Windows
```bash 
python -m venv venv
```
On macOS / Linux
```bash
python3 -m venv venv
```
### 3. Activate the virtual environment
On Windows
```bash
venv\Scripts\activate
```
On macOS / Linux
```bash
source venv/bin/activate
```
You should now see (venv) in your terminal.

### 4. Install dependencies
```bash
pip install -r requirements.txt
```
### 5. Install Playwright browsers
```bash
playwright install
```
This step downloads Chromium for headless browsing.

### 6. Running the Application
```bash
python cli.py
```
You should see:
```
Web Scraper CLI — type 'exit' to quit
>>>
```
<b>Available Commands</b>
| Command	| Description |
| -- | -- |
navigate <url> | Open a new webpage
show title	| Display the page title
show code	| Display full HTML source
capture <css_selector>	| Extract HTML using CSS selector
click <css_selector> | Click an element
back | Navigate to previous page
exit | Close the browser and exit

<b>Example Session</b>
```
>>> navigate https://example.com
>>> show title
Example Domain
>>> capture h1
<h1>Example Domain</h1>
>>> exit
```

## Running with Docker (Recommended)
1. Build the Docker image
docker build -t webscraper-cli .

2. Run with PostgreSQL
docker run -it --rm \
  -e DATABASE_URL=postgresql://user:password@host.docker.internal:5432/web_scraper \
  -e HEADLESS=true \
  webscraper-cli


Docker runs headless by default — no GUI required.

## Notes & Best Practices
- Headful mode requires an X server (not supported in Docker)
- Some websites block automation (403 Forbidden)
- Respect website robots.txt and Terms of Service
- Use proxies and realistic user agents when needed
- JavaScript-heavy websites are fully supported.

## License
