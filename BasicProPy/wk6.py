def mystery3(x):
    y = 1
    z = 2
    next = int(input("Type a number: "))

    # Point A
    while next >= 0:
        # Point B
        if y >= z:
            # Point C
            z = y
        
        y += 1
        next = int(input("Type a number: "))
        # Point D

    # Point E
    return z

def main():
    for i in range(-3, 3):
        print(i, end='')
        print(mystery3(i))

main()