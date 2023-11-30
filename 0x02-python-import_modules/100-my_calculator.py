#!/usr/bin/python3
from sys import argv
from calculator_1 import sub, add, mul, div

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, operator, b = argv[1:]

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        exit(1)

    if operator == "*":
        result = mul(a, b)
    elif operator == "+":
        result = add(a, b)
    elif operator == "/":
        result = div(a, b)
    elif operator == "-":
        result = sub(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))
