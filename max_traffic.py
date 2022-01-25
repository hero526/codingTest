import math
def get_elapsed_time(base, time, duration):  
    hour, minute, sec = time.split(':')
    
    hour_diff = int(hour) - base[0]
    minute_diff = int(minute) - base[1]
    sec_diff = float(sec) - base[2]
    
    end = (hour_diff * 60 * 60) + (minute_diff * 60) + sec_diff
    start = end - duration + 0.001
    return (start, end)
    
    
def solution(lines):
    answer = 1
    timeset = []
    base = (lines[0].split()[1].split(':'))
    base[0] = int(base[0])
    base[1] = int(base[1])
    base[2] = float(base[2])
    
    for line in lines:
        time, duration = line.split()[1:]
        duration = float(duration[:-1])
        start, end = get_elapsed_time(base, time, duration)
        
        timeset.append((round(start,3), round(end,3)))
    
    for i in range(len(timeset)):
        print(timeset[i])
        cnt = 1
        for j in range(len(timeset)):
            if i == j:
                continue
            # i의 시작지점으로부터 1초간 몇개의 request가 있었는가
            if timeset[j][0] - timeset[i][0] < 1 and timeset[j][0] - timeset[i][0] > 0:
                cnt += 1
            elif timeset[j][1] - timeset[i][0] < 1 and timeset[j][1] - timeset[i][0] > 0:
                cnt += 1
            elif timeset[i][0] >= timeset[j][0] and timeset[i][0] + 1 <= timeset[j][1]:
                cnt += 1
        
        if answer < cnt:
            answer = cnt
        
        cnt = 1
        for j in range(len(timeset)):
            if i == j:
                continue
            # i의 끝지점으로부터 1초간 몇개의 request가 있었는가
            if timeset[j][0] - timeset[i][1] < 1 and timeset[j][0] - timeset[i][1] > 0:
                cnt += 1
            elif timeset[j][1] - timeset[i][1] < 1 and timeset[j][1] - timeset[i][1] > 0:
                cnt += 1
            elif timeset[i][1] >= timeset[j][0] and timeset[i][1] + 1 <= timeset[j][1]:
                cnt += 1
        
        if answer < cnt:
            answer = cnt
        
    return answer
