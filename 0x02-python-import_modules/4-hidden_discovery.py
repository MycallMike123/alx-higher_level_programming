#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    the_names = dir(hidden_4)

    for name in the_names:
        if not name.startswith("__") and \
                not hasattr(getattr(hidden_4, name), '__call__'):
            print(the_name)
