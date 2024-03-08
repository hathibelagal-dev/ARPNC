from util.stack import Stack

keywords = "drop + - * / dup print".split(" ")
stack = Stack()
text = "2 3 + 5 5 * - 2 * dup * dup print 2 * print"

tokens = text.split(" ")

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
    if token not in keywords:
        stack.push(token)
    else:
        handle_token(token)

print(stack)
