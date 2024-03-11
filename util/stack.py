import re

class Stack:    
    def __init__(self):
        self.data = []

    def dup(self):
        if len(self.data) > 0:
            latest_item = self.data[-1]
            self.data.append(latest_item)

    def drop(self):
        if len(self.data) > 0:
            self.data.pop()

    def push(self, x):
        if type(x) is str and re.match(r'^[+-]?\d+(>?\.\d+)?$', x):
            x = float(x)
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def __repr__(self):
        if self.data:
            return f"Stack still has data: {self.data}"
        return "ok"
