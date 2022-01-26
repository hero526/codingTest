from itertools import permutations

def solution(expression):
    answer = 0
    
    cal = [x for x in expression if not x.isdigit()]
    number = []
    
    num = ''
    for digit in expression:
        if digit.isdigit():
            num += digit
        else:
            number.append(num)
            num = ''
    number.append(num)
    
    case = set(cal)
    for order in permutations(case, len(case)):
        cur_number = number.copy()
        cur_cal = cal.copy()
        for operand in order:
            idx = 0
            while idx < len(cur_cal):
                if cur_cal[idx] == operand:
                    cur_number[idx] = str(eval(cur_number[idx] + cur_cal[idx] + cur_number[idx+1]))
                    del cur_number[idx+1]
                    del cur_cal[idx]
                    idx -= 1
                idx+=1
        if abs(int(cur_number[0])) > answer:
            answer = abs(int(cur_number[0]))
    return answer
