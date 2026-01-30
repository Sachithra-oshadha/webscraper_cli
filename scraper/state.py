class BrowserState:
    def __init__(self):
        self.current_url = None
        self.html = None
        self.title = None
        self.history = []
        self.forward_stack = []

    def update(self, url, html, title):
        if self.current_url:
            self.history.append(self.current_url)
        self.current_url = url
        self.html = html
        self.title = title
        self.forward_stack.clear()
