def startNend():
    print("+", end="")
    for line in range(1, 9):
        print("-", end="")
    print("+")



def middle1():
    height = 4
    count = 7
    for num in range(1, height+1):
        print("|", end="")
        print(" "*(num-1), end="")
        print("\\", end="")
        for i in range (1, count):
            if (count != i):
                print(i, end="")
            
        print("/", end="")
        print(" "*(num-1), end="")
        print("|")
        count-=2


def middle2():
    height = 4
    count = 1
    blankcount = 3
    for num in range(1, height+1):
        print("|", end="")
        print(" "*blankcount, end="")
        print("/", end="")
        for i in range (1, count):
            if (count == i):
                print("/\\", end="")
            else:
                print(i, end="")
            
        print("\\", end="")
        print(" "*blankcount, end="")
        print("|")
        count += 2
        blankcount -= 1


1*0
1*1
1*2

startNend()
middle1()
startNend()

startNend()
middle2()
startNend()

# +--------+
# |\123456/|
# | \1234/ |
# |  \12/  |
# |   \/   |
# +--------+