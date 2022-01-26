def J(set1, set2):
    intersection = []
    union = []
    for item in set1:
        if item in set2:
            del set2[set2.index(item)]
            intersection.append(item)
        else:
            union.append(item)
    union += intersection + set2
    
    if union:
        return len(intersection)/len(union)
    else:
        return 1


def solution(str1, str2):
    answer = 0
    
    set1 = [str1.lower()[i:i+2] for i in range(len(str1)-1)]
    set2 = [str2.lower()[i:i+2] for i in range(len(str2)-1)]
    
    new_set = []
    for item in set1:
        if item.isalpha():
            new_set.append(item)
    set1 = new_set

    new_set = []
    for item in set2:
        if item.isalpha():
            new_set.append(item)
    set2 = new_set
    
    answer = int(J(set1, set2) * 65536)
    
    return answer
