def print_num_range(num1, num2):
    list = []
    if (num1 < num2):
        for i in range(num1, num2+1):
            list.append(i)
    elif (num1 > num2):
        for i in range(num1, num2-1, -1):
            list.append(i)
    else:
        list.append(num1)
    
    print(list)

print_num_range(2, 7)
print_num_range(19, 11)
print_num_range(5, 5)
