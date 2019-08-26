import copy
from Project_3.helpers.Merge_Sort import merge_sort


def rearrange_digits(input_list):
    if len(input_list) == 1 or len(input_list) == 0 or input_list is None:
        return None

    sorted_array = merge_sort(input_list)
    copy_sorted = copy.deepcopy(sorted_array)
    string_1 = ""
    string_2 = ""

    while copy_sorted:
        if len(string_1) == len(string_2):
            string_1 += str(copy_sorted[-1])
            copy_sorted.pop()
        elif len(string_1) > len(string_2):
            string_2 += str(copy_sorted[-1])
            copy_sorted.pop()
    return [int(string_1), int(string_2)]

