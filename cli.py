from scraper.browser import Browser
from scraper.state import BrowserState
from scraper.navigator import Navigator
from scraper.commands import CommandHandler
from scraper.db import DatabaseLogger

def main():
    browser = Browser()
    state = BrowserState()

    db_logger = DatabaseLogger(
        dsn="dbname=web_scraper user=postgres password=postgres host=host.docker.internal port=5432"
    )

    navigator = Navigator(browser, state, db_logger)
    handler = CommandHandler(navigator, state, browser)

    print("Web Scraper CLI — type 'exit' to quit")

    while True:
        command = input(">>> ")
        handler.handle(command)

if __name__ == "__main__":
    main()