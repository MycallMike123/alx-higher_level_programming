#!/usr/bin/python3

def magic_calculation(a, b, c):
    if b > a:
        return c
    elif c < b:
        return a + b
    return a * b - c
