#!/usr/bin/python3

def remove_char_at(str, n):
    if 0 <= n < len(str):
        res_str = str[:n] + str[n + 1:]
        return res_str
    else:
        return str
