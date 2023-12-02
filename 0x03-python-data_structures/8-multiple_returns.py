#!/usr/bin/python3

def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len > 0:
        letter = sentence[0]
    else:
        return (0, None)

    result = str_len, letter
    return result
