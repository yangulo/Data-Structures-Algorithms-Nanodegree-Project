def binary_search(array, target):
    return recursive_binary_search(array, target, 0, len(array))


def recursive_binary_search(array, target, start, end):
    if len(array) == 0 or start > end:
        return None

    mid = (start + end)//2
    if array[mid] == target:
        return mid
    if array[mid] > target:
        return recursive_binary_search(array, target, start, mid-1)
    else:
        return recursive_binary_search(array, target, mid + 1, end)
