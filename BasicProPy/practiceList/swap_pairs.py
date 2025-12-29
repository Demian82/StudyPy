def swap_pairs(lst: list):

    for i in range(0, len(lst), 2):
        if i+1<len(lst):
            lst.insert(i+1, lst.pop(i))

    print(lst)

def swap(a, b):
    temp = a
    a = b
    b = temp
    lst = [a, b]
    return lst

a = ["a", "bb", "c", "ddd", "f", "ee", "g"]
swap_pairs(a)
