def min_to_front(a: list):
    min_value = min(a)
    min_index = a.index(min_value)
    a.insert(0, a.pop(min_index))
    return a