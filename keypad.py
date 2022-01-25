def get_distance(cur, target):
    distance = 0
    while abs(cur-target) >= 3:
        distance += 1
        if cur > target:
            cur -= 3
        else:
            cur += 3
    
    distance += abs(cur-target)
    return distance


def solution(numbers, hand):
    answer = ''
    
    left = 10
    right = 12
    
    for number in numbers:
        if number == 0:
            number = 11
        if number in [1, 4, 7]:
            left = number
            answer += 'L'
        elif number in [3, 6, 9]:
            right = number
            answer += 'R'
        else:
            left_distance = get_distance(left, number)
            right_distance = get_distance(right, number)
            
            if left_distance > right_distance:
                right = number
                answer += 'R'
            elif right_distance > left_distance:
                left = number
                answer += 'L'
            else:   # same distance
                if hand == 'right':
                    right = number
                    answer += 'R'
                else:
                    left = number
                    answer += 'L'
            
    return answer
