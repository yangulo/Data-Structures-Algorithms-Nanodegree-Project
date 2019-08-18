import os


def find_files(suffix, path):
    if len(path) == 0:
        return -1
    return find_files_recursive(suffix, path, list())


def find_files_recursive(suffix, path, new_arr):
    arr = os.listdir(path)
    for element in arr:
        new_path = path + "/" + element
        if os.path.isfile(new_path):
            if element.endswith(suffix):
                new_arr.append(new_path)
        else:
            find_files_recursive(suffix, new_path, new_arr)
    if len(new_arr) == 0:
        return -1
    return new_arr

