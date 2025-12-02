def show_tows(num):
    operand = num
    count = 0
    while(operand % 2 == 0 or num == 0):
        operand = operand // 2
        count += 1
    
    print(f"{num} = ", end='')
    for i in range(0, count):
        print("2 * ", end='')
    print(f'{operand}')


show_tows(7)
show_tows(18)
show_tows(68)
show_tows(120)