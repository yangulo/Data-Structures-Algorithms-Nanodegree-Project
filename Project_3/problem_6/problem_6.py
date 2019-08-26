def get_min_max(ints):
    if ints is None or len(ints) == 0 or len(ints) == 1:
        return None

    max_element = ints[0]
    min_element = ints[0]

    for element in range(1, len(ints)):
        if max_element < ints[element]:
            max_element = ints[element]
        if min_element > ints[element]:
            min_element = ints[element]
    return min_element, max_element
