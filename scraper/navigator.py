class Navigator:
    def __init__(self, browser, state, db_logger=None):
        self.browser = browser
        self.state = state
        self.db_logger = db_logger

    def navigate(self, url):
        html, title = self.browser.navigate(url)
        self.state.update(url, html, title)

        if self.db_logger:
            self.db_logger.log_page_visit(url, html)

    def back(self):
        if not self.state.history:
            raise Exception("No history available")
        last = self.state.history.pop()
        self.state.forward_stack.append(self.state.current_url)
        html, title = self.browser.navigate(last)
        self.state.current_url = last
        self.state.html = html
        self.state.title = title
