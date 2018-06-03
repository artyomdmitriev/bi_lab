def division_by_zero():
    try:
        print(5 / 0)
    except ZeroDivisionError as zde:
        for err in zde.args:
            print(err)


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as ie:
        for err in ie.args:
            print(err)


def add_to_list_in_dict(thedict, listname, element):
    try:
        length = thedict[listname]
        print("%s already has %d elements." % (listname, len(length)))
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


# test division by zero
division_by_zero()

# test index error
print_list_element([1, 2, 3], 5)

# test dict
dictionary = {'a': [1, 2, 3]}
add_to_list_in_dict(dictionary, 'c', 4)
