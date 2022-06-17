#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ Replaces an element of a list at a specific position."""
    if idx < 0:
        return my_list

    if idx >= len(my_list):
        return my_list

    for index in range(len(my_list)):
        if index == idx:
            my_list[index] = element
            return my_list
