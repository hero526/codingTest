def solution(record):
    username = dict()
    result = []
    answer = []
    for log in record:
        data = log.split()
        cmd = data[0]
        user_id = data[1]
        
        if cmd == "Enter":
            nickname = data[2]
            username[user_id] = nickname
            result.append((user_id,cmd))
        elif cmd == "Leave":
            result.append((user_id,cmd))
        elif cmd == "Change":
            nickname = data[2]
            username[user_id] = nickname
        else:
            print("Unknown Command")
    
    for user_id, cmd in result:
        if cmd == "Enter":
            answer.append(f'{username[user_id]}님이 들어왔습니다.')
        else:
            answer.append(f'{username[user_id]}님이 나갔습니다.')
    
    return answer
