#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    the_names = dir(hidden_4)

    for the_name in names:
        if the_name[:2] != "__":
            print(the_name)
