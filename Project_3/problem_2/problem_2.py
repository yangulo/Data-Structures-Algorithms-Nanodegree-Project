def rotated_array_search(input_list, number):
    if input_list is None or len(input_list) == 0:
        return None
    return recursive_rotated_array_search(input_list, number, 0, len(input_list) - 1)


def recursive_rotated_array_search(array, target, start_index, end_index):
    mid_index = (start_index + end_index) // 2

    if array[mid_index] == target:
        return mid_index

    if start_index >= end_index:
        return -1

    if target < array[mid_index]:
        if array[start_index] < array[mid_index] and array[start_index] <= target:
            return recursive_rotated_array_search(array, target, start_index, mid_index - 1)
        else:
            return recursive_rotated_array_search(array, target, mid_index + 1, end_index)
    if target > array[mid_index]:
        if array[end_index] > array[mid_index] and array[end_index] >= target:
            return recursive_rotated_array_search(array, target, mid_index + 1, end_index)
        else:
            return recursive_rotated_array_search(array, target, start_index, mid_index - 1)
