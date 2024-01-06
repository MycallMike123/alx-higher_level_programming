#!/usr/bin/python3

def text_indentation(text):
    """ Prints a text with 2 lines after each character """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = (
            text.replace(".", ".\n\n")
            .replace("?", "?\n\n")
            .replace(":", ":\n\n")
    )

    lines = text.split('\n')
    for line in lines:
        print(line.strip())
