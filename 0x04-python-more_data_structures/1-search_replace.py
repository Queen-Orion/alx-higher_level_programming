#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurences of an element by another in a new list.
    """

    return list(map(lambda v: v if v != search else replace, my_list))
