from scraper.browser import Browser
from scraper.state import BrowserState
from scraper.navigator import Navigator
from scraper.commands import CommandHandler
from scraper.db import DatabaseLogger
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    browser = Browser()
    state = BrowserState()

    db_logger = DatabaseLogger(
        dsn=f"dbname={os.getenv('DATABASE_NAME')} user={os.getenv('DATABASE_USER')} password={os.getenv('DATABASE_PASSWORD')} host={os.getenv('DATABASE_HOST')} port={os.getenv('DATABASE_PORT')}"
    )

    navigator = Navigator(browser, state, db_logger)
    handler = CommandHandler(navigator, state, browser)

    print("Web Scraper CLI — type 'exit' to quit")

    while True:
        command = input(">>> ")
        handler.handle(command)

if __name__ == "__main__":
    main()