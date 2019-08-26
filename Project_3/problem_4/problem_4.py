def sort_012(input_list):
    if input_list is None or len(input_list) < 3:
        return None
    current = 0
    left_index = 0
    right_index = len(input_list) - 1
    i = -1
    while left_index < len(input_list):
        if input_list[left_index] > input_list[right_index]:
            tmp = input_list[left_index]
            input_list[left_index] = input_list[right_index]
            input_list[right_index] = tmp
        if current == input_list[left_index]:
            left_index += 1
        if left_index >= right_index:
            i = 1
        right_index += i
        if right_index == len(input_list):
            right_index = len(input_list) - 1
            i = -1
            current += 1
