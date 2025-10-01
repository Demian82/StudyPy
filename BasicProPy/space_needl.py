LINE = 4

def main():
    spear()
    roof()
    cup()
    spear()
    column()
    roof()

def spear():
    for i in range(1,LINE+1):
        for j in range(1, LINE*3+1):
            print(' ' , end='')
        print('||')

def roof():
    for i in range(1,LINE+1):
        for space in range(1, i * -3 + (LINE*3)+1):
            print(' ', end='')
        print('__/', end='')

        colon(i-1)
        print('||', end='')
        colon(i-1)
        print('\\__')
    print('|', end='')
    for comma in range(1, LINE*6+1):
        print('"', end='')
    print('|')
        
        
def colon(num):
    for colon in range(0,num):
        print(':::', end='')

def cup():
    for i in range(1, LINE+1):
        for space in range(1, i):
            print('  ', end='')
        print('\\_/', end='')
        for v in range(1, i*-2 + (LINE*3) + 1):
            print('\\/', end='')
        print('\\_/')


def column():
    for looping in range(1, LINE+1):
        for i in range(1,LINE+1):
            for j in range(1, LINE*2+2):
                print(' ', end='')
            print('|%%||%%|')


main()