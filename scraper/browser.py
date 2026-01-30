from playwright.sync_api import sync_playwright

REALISTIC_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/121.0.0.0 Safari/537.36"
)

class Browser:
    def __init__(self, proxy=None):
        self.playwright = sync_playwright().start()

        launch_args = {
            "headless": True,
        }

        if proxy:
            launch_args["proxy"] = {
                "server": proxy
            }

        self.browser = self.playwright.chromium.launch(**launch_args)

        self.context = self.browser.new_context(
            user_agent=REALISTIC_USER_AGENT,
            viewport={"width": 1280, "height": 800}
        )

        self.page = self.context.new_page()
        self.page.set_default_timeout(60000)

    def navigate(self, url):
        self.page.goto(url, wait_until="domcontentloaded")
        return self.page.content(), self.page.title()

    def click(self, selector):
        self.page.click(selector)
        self.page.wait_for_load_state("domcontentloaded")
        return self.page.content(), self.page.title()

    def close(self):
        self.browser.close()
        self.playwright.stop()
