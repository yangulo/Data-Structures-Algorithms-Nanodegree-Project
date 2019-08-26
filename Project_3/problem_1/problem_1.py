def sqrt(number):
    if number is None or isinstance(number, str):
        return None

    if number == 1 or number == 0:
        return number

    number = int(number)
    start = 0
    end = number
    return recursive_sqrt(number, start, end)


def recursive_sqrt(number, start, end):
    mid = (start + end) // 2

    if number//mid == mid:
        return mid
    else:
        num = number // mid
        if num < mid:
            # Go down
            return recursive_sqrt(number, start, mid - 1)
        else:
            # Go up
            return recursive_sqrt(number, mid + 1, end)
