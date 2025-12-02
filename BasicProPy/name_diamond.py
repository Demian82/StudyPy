def name_diamond(name):
    for i in range(0, len(name)):
        print(name[:i+1])
    for j in range(0, len(name)):
        if (j+1 == len(name)):
            return -1
        else:
            print(' '*(j+1), end='')
            print(name[j+1:])

name_diamond("MARTY")