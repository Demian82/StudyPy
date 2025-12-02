numbers = [3, 4]
our_score = [85, 93]
score_list = [85, 92, 38, 93, 48, 85, 92, 56]

def solution(numbers, our_score, score_list):
    answer = []
    length = len(numbers)
    for i in range(length):
        num = numbers[i]
        if our_score[i] == score_list[num-1]:
            answer.append("Same")
        else:
            answer.append("Diff")
    print(answer)

solution(numbers, our_score, score_list)