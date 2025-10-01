# num이 0이거나 양수라면 num을 반환
def func1(num):
    if 0>num:
        return 0
    else:
        return num

# num이 0이거나 음수라면 num을 반환
def func2(num):
    if num > 0:
        return 0
    else:
        return num

# off, 내린 사람의 수
def func3(station):
    num = 0
    for people in station:
        if people == "Off":
            num+=1
    return num

# on, 탄 사람의 수
def func4(station):
    num = 0
    for people in station:
        if people == "On":
            num += 1
    return num

def solution(seat, passengers):
    num_passenger = 0
    for station in passengers:
        num_passenger += func4(station)
        num_passenger -= func3(station)
    answer = func1(seat-num_passenger)
    return answer

def main():
    seat = 5
    passengers = [["On", "On", "On"], ["Off", "On", "-"], ["Off", "-", "-"]]
    
    print(solution(seat, passengers))

main()