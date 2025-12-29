def list_mystery2(a):
    for i in range(1, len(a)-1):
        a[i] = a[i-1] - a[i] + a[i+1]
    print(a)

# a3=[7, 7, 3, 8, 2]

# list_mystery2(a3)
# a4 = [4, 2, 3, 1, 2, 5]
# list_mystery2(a4)
# a5 = [6, 0, -1, 3, 5, 0, -3]
# list_mystery2(a5)

def mystery(a, b, c):
    b = b+c
    for i in range(len(a)):
        a[i] += 1
    c = c+a[0]
    print(a, b, c)

def main():
    a = [10, 20]
    b = 3
    c = 5

    mystery(a, b, c)
    print(a, b, c)

    a[1] += 1
    mystery(a, a[0], b)
    print(a, b, c)

main()