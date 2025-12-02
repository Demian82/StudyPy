def days_in_month(month):
    if (month == 2):
        return 28
    
    if (month<=7):
        if (month % 2 == 0):
            return 30
        else:
            return 31
    else:
        if (month % 2 == 0):
            return 31
        else:
            return 30
        
def main():
    for i in range(1,13):
        days = days_in_month(i)
        print(days)

main()