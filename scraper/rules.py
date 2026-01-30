class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, action):
        self.rules.append((condition, action))

    def evaluate(self, html):
        for condition, action in self.rules:
            if condition(html):
                action(html)
