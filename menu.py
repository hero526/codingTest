from itertools import combinations

def solution(orders, course):
    answer = []
    
    for length in course:
        candidates = dict()
        for order in orders:
            for menu in combinations(order, length):
                result = ''.join(sorted(menu))
                if result in candidates:
                    candidates[result] += 1
                else:
                    candidates[result] = 1
        if candidates:
            max_count = max(candidates.values())
            answer += [item for item, count in candidates.items() if count > 1 and count == max_count]
            
    return sorted(answer)
