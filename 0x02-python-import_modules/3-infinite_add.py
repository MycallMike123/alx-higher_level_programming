#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments = argv[1:]

    res = sum(int(arg) for arg in arguments)

    print(res)
