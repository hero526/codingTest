def solution(s):
    answer = ""
    min_length = len(s)
    
    for unit in range(1,len(s)//2+1):
        splitted = []
        compressed = ""
        for i in range(0,len(s),unit):
            splitted.append(s[i:i+unit])
        
        head = splitted[0]
        cnt = 1
        for cur in splitted[1:]:
            if cur == head:
                cnt+=1
            else:
                if cnt != 1:
                    compressed = compressed + str(cnt)
                compressed = compressed + head
                cnt = 1
                head = cur
        if cnt != 1:
            compressed = compressed + str(cnt)
        compressed = compressed + cur
        
        if len(compressed) < min_length:
            min_length = len(compressed)

    return min_length
