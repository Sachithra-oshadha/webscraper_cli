# Web Scraper CLI

An interactive command-line web scraper that uses a real headless browser to navigate websites, interact with elements, and extract HTML content using CSS selectors.

Unlike basic scrapers, this tool supports JavaScript-rendered pages and simulates real user interactions such as clicks and navigation.

---

## Features

- Navigate to any website
- Display page title and HTML source
- Capture specific HTML sections using CSS selectors
- Click elements programmatically
- Maintain browser navigation history
- Extensible command-based architecture
- Headless browser automation using Playwright

---

## Prerequisites

- Python **3.10 or higher**
- pip (Python package manager)

---

## Setup Using a Virtual Environment

### 1. Clone the repository

```bash
git clone https://github.com/your-username/webscraper-cli.git
cd webscraper-cli
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
## Notes

This project uses headless Chromium, so no browser window is displayed.

JavaScript-heavy websites are fully supported.

Always respect website terms of service when scraping.

## License