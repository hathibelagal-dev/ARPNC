import re

class Stack:    
    def __init__(self):
        self.data = []

    def dup(self):
        if len(self.data) > 0:
            latest_item = self.data[-1]
            self.data.append(latest_item)

    def peek(self):
        if len(self.data) > 0:
            print(self.data[-1])
        else:
            print("Stack empty")

    def drop(self):
        if len(self.data) > 0:
            self.data.pop()

    def push(self, x):
        if type(x) is str and re.match(r'^[+-]?\d+(>?\.\d+)?$', x):
            x = float(x)
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def pop2(self):
        return [self.data.pop(), self.data.pop()]

    def print(self, show_contents = True):
        output = None
        if self.data:
            output = f"Stack has data: {self.data}"
        else:
            output = "ok"            
        if show_contents:
            print(output)
