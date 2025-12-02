def fileIO(fileName):
    with open(fileName, 'r') as f:
        content = f.read()
    
    return content

def worktime(lst):
    total = 0
    for t in lst:
        total+=float(t)
    return total

def hours():
    fileName = input("Input file? ")
    content = fileIO(fileName).split("\n")
    for e in content:
        if not e.strip():
            continue
        employee = e.split()
        id = str(employee[0])
        name = employee[1]
        work = employee[2:]
        t_work = worktime(work)
        d_work = len(work)
        print(f'{name} (ID#{id}) worked {t_work:.1f} hours ({t_work / d_work:.1f}/day)')

hours()