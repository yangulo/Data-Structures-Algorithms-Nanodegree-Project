from Project_2.problem_1.DoubleLinkedList import DoubleLinkedList


def union(dll_1, dll_2):
    if dll_1 is None and dll_2 is None:
        return None
    if dll_1.size == 0:
        return dll_2
    elif dll_2.size == 0:
        return dll_1
    elif dll_1.size == 0 and dll_2.size == 0:
        return list()

    union_dll = DoubleLinkedList()
    for element in dll_2:
        union_dll.append(element)
    for element in dll_1:
        union_dll.append(element)
    return union_dll


def intersection(dll_1, dll_2):
    if dll_1 is None or dll_2 is None or dll_1.size() == 0 or dll_2.size() == 0:
        return None

    inter_dll = DoubleLinkedList()
    copy_dll_1 = DoubleLinkedList()
    for element in dll_1:
        copy_dll_1.append(element)

    for element in dll_2:
        if element in copy_dll_1:
            inter_dll.append(element)
            copy_dll_1.remove_element(element)
    return inter_dll
