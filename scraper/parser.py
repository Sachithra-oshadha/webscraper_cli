from bs4 import BeautifulSoup

class HTMLParser:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "lxml")

    def capture(self, selector):
        elements = self.soup.select(selector)

        if not elements:
            return {
                "success": False,
                "message": f"No elements matched selector: '{selector}'",
                "results": []
            }

        return {
            "success": True,
            "message": f"{len(elements)} element(s) matched",
            "results": [str(el) for el in elements]
        }
