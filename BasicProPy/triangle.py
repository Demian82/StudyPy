def triangle(len):
    for i in range(1,len+1):
        for space in range(1, len+1 -i):
            print(' ', end='')
        print('*'*i)

triangle(5)