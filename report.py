def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    
    relation = [[0 for i in range(len(id_list))] for i in range(len(id_list))]    
    
    for r in list(set(report)):
        reporter, reportee = r.split()
        relation[id_list.index(reportee)][id_list.index(reporter)] += 1
        
    for i in range(len(id_list)):
        if sum(relation[i]) >= k:
            for j in range(len(id_list)):
                if relation[i][j] != 0:
                    answer[j] += 1
    
    return answer
