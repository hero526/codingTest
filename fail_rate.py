def solution(N, stages):
    answer = []
    
    fail = dict()
    challenged = len(stages)
    for i in range(1, N+1):
        stuck = stages.count(i)
        if challenged:
            fail[i] = stuck / challenged
            challenged -= stuck
        else:
            fail[i] = 0
            
    answer = sorted(fail, key=lambda x:-fail[x])
            
    return answer
