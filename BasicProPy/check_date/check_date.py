def check_dates(fileName: str):
    f = open(fileName, 'r')
    c = f.read()
    d = c.split('\n')
    for dates in d:
        day = dates.split()
        if(len(day)<4 or day[0]==' '):
            return
        diff = differ_day(day[0], day[1], day[2], day[3])
        if (diff == 1):
            print(f'{day[0]}/{day[1]} and {day[2]}/{day[3]} '
                  'differ by one full month or more!')
        else:
            print(f'{day[0]}/{day[1]} and {day[2]}/{day[3]} '
                  'are within one month of each other.')
        
def differ_day(m1, d1, m2, d2):
    m1 = int(m1)
    d1 = int(d1)
    m2 = int(m2)
    d2 = int(d2)
    if (abs(m1-m2)>1):
        return 1
    # over a month
    else:
        if (m1 < m2):
            if (d1 < d2):
                return 1
            # over a month
            elif (d1 > d2):
                return 0
            # less a month
            else:
                return 1
            # a month
        elif (m1 > m2):
            if (d1 < d2):
                return 0
            # less a month
            elif (d1 > d2):
                return 1
            # over a month
            else:
                return 1
            # a month
        else:
            return 0
        # m1 = m2, less a month

check_dates('dates.txt')