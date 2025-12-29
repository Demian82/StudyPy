def repeat(lst: list, k: int):
    if k<=0:
        lst.clear()
        return
    
    r_list=[]
    for word in lst:
        r_list.extend([word] * k)
    
    lst[:] = r_list

repeat(["how", "are", "you?"], 4)