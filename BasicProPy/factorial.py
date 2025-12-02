def factorial(num):
    fctrl = 1
    for i in range(1, num+1):
        fctrl *= i
    print(f'{num} factorial = {fctrl}')

factorial(4)