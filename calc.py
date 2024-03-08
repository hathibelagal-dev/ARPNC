from util.stack import Stack
from util.cleanup import *
import sys

keywords = "drop + - * / dup print".split(" ")
stack = Stack()

if len(sys.argv) < 2:
    print("No input provided")
    sys.exit(1)

text = None
with open(sys.argv[1], "r") as f:
    text = f.read()

tokens = cleanup(text).split(" ")

def handle_token(op):
    if op == "+":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(i1 + i2)

    if op == "-":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(i1 - i2)

    if op == "*":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(i1 * i2)

    if op == "/":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(i1 / i2)

    if op == "dup":
        stack.dup()

    if op == "print":
        i1 = stack.pop()
        print(i1)

for token in tokens:
    if not token:
        continue
    if token not in keywords:
        stack.push(token)
    else:
        handle_token(token)

print(stack)
