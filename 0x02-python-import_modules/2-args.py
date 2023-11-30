#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arguments_number = len(argv) - 1
    
    if arguments_number > 0:
        print("{} argument{}:".format(arguments_number,
            's' if arguments_number != 1 else ''))

        for i, _argument in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, _argument))

    else:
        print("{} argument{}".format(arguments_number,
            's.' if arguments_number == 0 else ''))
