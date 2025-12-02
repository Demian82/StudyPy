def biggest_and_smallest(times):
    list = []
    for i in range(0, int(times)):
        num = int(input("Next number? "))
        list.append(num)

    biggest = list[0]
    for big in range(1, len(list)):
        if (biggest < list[big]):
            biggest = list[big]
    
    smallest = list[0]
    for small in range(1, len(list)):
        if (smallest > list[small]):
            smallest = list[small]
        
    print(f"Biggest = {biggest}")
    print(f"Smallest = {smallest}")

def main():
    times = input("How many numbers? ")
    biggest_and_smallest(times)

main()