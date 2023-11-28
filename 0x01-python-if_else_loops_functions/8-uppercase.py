#!/usr/bin/python3

def uppercase(str):
    for alph in str:
        if ord("a") <= ord(alph) <= ord("z"):
              alph = chr(ord(alph) - 32)
        print("{:s}".format(alph), end="")
    print()
