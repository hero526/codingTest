def solution(s):
    answer = []
    
    s = s[2:-2].split('},{')
    
    for i in range(len(s)):
        s[i] = s[i].split(',')
        for j in range(len(s[i])):
            s[i][j] = int(s[i][j])
            
    s = sorted(s, key=lambda x: len(x))
        
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            del s[j][s[j].index(s[i][0])]
        answer.append(s[i][0])
    
    return answer
