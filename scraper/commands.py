from rich import print
from scraper.parser import HTMLParser

class CommandHandler:
    def __init__(self, navigator, state, browser):
        self.navigator = navigator
        self.state = state
        self.browser = browser

    def handle(self, command):
        if not command.strip():
            return

        parts = command.split()
        cmd = parts[0]
        if cmd == "navigate":
            self.navigator.navigate(parts[1])
            print(f"[green]Loaded:[/green] {self.state.title}")

        elif cmd == "show":
            if parts[1] == "code":
                print(self.state.html)
            elif parts[1] == "title":
                print(self.state.title)

        elif cmd == "capture":
            parser = HTMLParser(self.state.html)
            result = parser.capture(" ".join(parts[1:]))
            if not result["success"]:
                print(f"[yellow]{result['message']}[/yellow]")
            else:
                for r in result["results"]:
                    print(r)


        elif cmd == "click":
            html, title = self.browser.click(" ".join(parts[1:]))
            self.state.update(self.browser.page.url, html, title)

        elif cmd == "exit":
            self.browser.close()
            exit()

        else:
            print("[red]Unknown command[/red]")
