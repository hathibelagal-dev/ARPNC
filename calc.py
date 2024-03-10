import math
from util.stack import Stack
from util.cleanup import *
import sys
from keywords import *
from operator import mul

variables = {}
functions = {}
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
    "current_string": "",
    "reading_function": False,
    "current_function": "",
    "current_function_token_num": None,
    "current_function_name": None
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

    elif op == ">":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(1 if i1 > i2 else 0)
        
    elif op == "<":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(1 if i1 < i2 else 0)
        
    elif op == "==":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(1 if i1 == i2 else 0)

    if op == "sum" or op == "product":
        data = []
        while True:
            data_item = stack.pop()
            if data_item == ".":
                break
            else:
                data.append(data_item)
        if op == "sum":
            stack.push(sum(data))
        else:
            result = 1
            for d in data:
                result *= d
            stack.push(result)

    if op == "not":
        i1 = stack.pop()
        stack.push(1 if not i1 else 0)

    if op == "swap":
        i1 = stack.pop()
        i2 = stack.pop()
        stack.push(i1)
        stack.push(i2)        
        
    if op == "e":
        i1 = stack.pop()
        stack.push(math.exp(i1))

    if op == "sqrt":
        i1 = stack.pop()
        stack.push(i1 ** 0.5)

    if op == "log2":
        i1 = stack.pop()
        stack.push(math.log2(i1))
        
    if op == "log":
        i1 = stack.pop()
        stack.push(math.log(i1))

    if op == "drop":
        stack.pop()

    if op == "sin":
        i1 = stack.pop()
        stack.push(math.sin(i1))
    
    if op == "cos":
        i1 = stack.pop()
        stack.push(math.cos(i1))

    if op == "tan":
        i1 = stack.pop()
        stack.push(math.tan(i1))

    if op == "dup":
        stack.dup()

    if op == "printnn":
        i1 = stack.pop()
        print(i1, end = "")

    if op == "space":
        stack.push(" ")

    if op == "print":
        i1 = stack.pop()
        print(i1)

    if op == "upper":
        i1 = stack.pop()
        stack.push(i1.upper())
    
    if op == "lower":
        i1 = stack.pop()
        stack.push(i1.lower())

    if op == "decr":
        i1 = stack.pop()
        stack.push(i1 - 1)

    if op == "incr":
        i1 = stack.pop()
        stack.push(i1 + 1)

    if op == "set":
        i1 = stack.pop()
        i2 = stack.pop()
        variables[i1] = i2

    if op == "$":
        if state["reading_string"]:
            stack.push(state["current_string"].strip())
            state["current_string"] = ""
            state["reading_string"] = False
        else:
            state["reading_string"] = True

    if op == "(":
        state["reading_function"] = True
        state["current_function_token_num"] = 0

    if op == ")":
        state["reading_function"] = False
        functions[state["current_function_name"]] = state["current_function"]
        state["current_function_name"] = None
        state["current_function"] = ""
        state["current_function_token_num"] = None

def iterate(tokens):
    try:
        for token in tokens:
            if not token:
                continue
            if state["reading_string"] and token != "$":
                state["current_string"] += " " + token
                continue
            if state["reading_function"] and token != ")":
                if not state["current_function_token_num"]:
                    state["current_function_name"] = token[1:]
                else:
                    state["current_function"] += " " + token
                state["current_function_token_num"] += 1
                continue
            if token not in keywords and token not in functions:
                if token.startswith("@"):
                    if token in variables:
                        token = variables[token]
                stack.push(token)
            elif token in functions:
                iterate(functions[token].split(" "))
            else:
                handle_token(token)
    except:
        print("Invalid program.")
        sys.exit(1)

iterate(tokens)

print(stack)
