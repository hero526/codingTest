def is_ok(people, partition):
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            if abs(people[i][0] - people[j][0]) + abs(people[i][1] - people[j][1]) <= 2: # too close
                if people[i][0] == people[j][0]: # vertical
                    if (people[i][0], (people[i][1] + people[j][1])/2) not in partition:
                        return 0
                elif people[i][1] == people[j][1]: # horizontal
                    if ((people[i][0] + people[j][0])/2, people[i][1]) not in partition:
                        return 0
                else: # cross
                    if (people[i][0]+1, people[i][1]) not in partition:
                        return 0
                    if people[i][1] > people[j][1]: # left side
                        if (people[i][0], people[i][1]-1) not in partition:
                            return 0
                    else: # right side
                        if (people[i][0], people[i][1]+1) not in partition:
                            return 0

            if people[i][0] - people[j][0] > 1: # no more close people
                break
    return 1


def solution(places):
    answer = []
    
    for place in places:
        people = []
        partition = []
        result = 1
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    people.append((i, j))
                elif place[i][j] == 'X':
                    partition.append((i, j))
        
        answer.append(is_ok(people, partition))
        
    return answer
