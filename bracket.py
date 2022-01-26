def solution(w):
    if len(w):
        cnt = 0
        is_correct = True
        for idx in range(len(w)):
            if w[idx] == '(':
                cnt += 1
            elif w[idx] == ')':
                cnt -= 1
            if cnt < 0:
                is_correct = False
            if cnt == 0:
                break
                
        u = w[:idx+1]
        v = solution(w[idx+1:])
                
        if is_correct:
            return u + v
        else:
            fixed = '(' + v + ')'
            for c in u[1:-1]:
                if c == '(':
                    fixed += ')'
                elif c == ')':
                    fixed += '('
            return fixed
    
    return ''
