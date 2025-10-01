SIZE = 4

def main():
    top_half()
    bottom_half()

def top_half():
    for line in range(1, SIZE + 1):
        print("|", end="")
        for space in range(1, (line * -2 + (2*SIZE)) + 1):
            print(" ", end="")
        print("<>", end="")

        for dot in range(1, (line * 4 - 4) + 1):
            print(".", end="")
        print("<>", end="")

        for space in range(1, (line * -2 + (2*SIZE)) + 1):
            print(" ", end="")
        print("|")

def bottom_half():
    for line in range(SIZE, 0, -1):
        print("|", end="")
        for space in range(1, (line * -2 + (2*SIZE)) + 1):
            print(" ", end="")
        print("<>", end="")

        for dot in range(1, (line * 4 - 4) + 1):
            print(".", end="")
        print("<>", end="")

        for space in range(1, (line * -2 + (2*SIZE)) + 1):
            print(" ", end="")
        print("|")

main()