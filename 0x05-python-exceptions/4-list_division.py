#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    final_list = []

    for elem in range(list_length):
        res = 0

        try:
            res = my_list_1[elem] / my_list_2[elem]

        except IndexError:
            print("out of range")

        except TypeError:
            print("wrong type")

        except ZeroDivisionError:
            print("division by 0")

        finally:
            final_list.append(res)

    return final_list
