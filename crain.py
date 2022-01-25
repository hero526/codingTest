def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves:
        move -= 1 # list index start from 0
        for level in board:
            if level[move] != 0: # doll found
                doll = level[move]
                level[move] = 0
                if len(basket) > 0 and basket[-1] == doll:
                    basket.pop()
                    answer += 2 # two dolls are eliminated
                else:
                    basket.append(doll)
                break
    
    return answer
