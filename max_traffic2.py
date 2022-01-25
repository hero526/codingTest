def get_elapsed_time(time, duration):  
    hour, minute, sec = time.split(':')
    
    hour_diff = int(hour) * 1000
    minute_diff = int(minute) * 1000
    sec_diff = int(float(sec) * 1000)
    
    end = (hour_diff * 60 * 60) + (minute_diff * 60) + sec_diff
    start = end - duration + 1
    return (start, end)
    
    
def solution(lines):
    answer = 1
    timeset = []
    
    for line in lines:
        time, duration = line.split()[1:]
        duration = int(float(duration[:-1]) * 1000)
        start, end = get_elapsed_time(time, duration)
        
        timeset.append((start, end))
    
    for i in range(len(timeset)):
        cnt = 1
        for j in range(i + 1, len(timeset)):
            # i의 끝지점으로부터 1초간 몇개의 request가 있었는가
            if timeset[j][0] - 1000 < timeset[i][1]:
                cnt += 1
                
        if answer < cnt:
            answer = cnt
        
    return answer
