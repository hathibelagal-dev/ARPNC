from util.stack import Stack
from util.cleanup import *
import sys

keywords = "drop + - * / ** dup print $ upper lower".split(" ")
stack = Stack()

if len(sys.argv) < 2:
    print("No input provided")
    sys.exit(1)

text = None
with open(sys.argv[1], "r") as f:
    text = f.read()

tokens = cleanup(text).split(" ")

state = {
    "reading_string": False,
    "current_string": ""
}

def handle_token(op):
    if op == "+":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(i1 + i2)

    elif op == "-":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(i1 - i2)

    elif op == "**":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(i1 ** i2)

    elif op == "*":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(i1 * i2)

    elif op == "/":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(i1 / i2)

    if op == "dup":
        stack.dup()

    if op == "print":
        i1 = stack.pop()
        print(i1)

    if op == "upper":
        i1 = stack.pop()
        stack.push(i1.upper())
    
    if op == "lower":
        i1 = stack.pop()
        stack.push(i1.lower())

    if op == "$":
        if state["reading_string"]:
            stack.push(state["current_string"].strip())
            state["current_string"] = ""
            state["reading_string"] = False
        else:
            state["reading_string"] = True

for token in tokens:
    if not token:
        continue
    if state["reading_string"] and token != "$":
        state["current_string"] += " " + token
        continue
    if token not in keywords:
        stack.push(token)
    else:
        handle_token(token)

print(stack)
