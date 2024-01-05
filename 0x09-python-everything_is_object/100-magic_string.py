#!/usr/bin/python3

def magic_string():
    magic = ""

    for a in range(1, 10):
        magic += "BestSchool" * a + ","

    return magic[:-1]
