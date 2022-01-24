def solution(s):
    answer = ""
    
    idx = 0
    while idx < len(s):
        if s[idx].isdigit():
            answer += s[idx]
            idx += 1
        elif s[idx:idx+4] == "zero":
            answer += "0"
            idx += 4
        elif s[idx:idx+3] == "one":
            answer += "1"
            idx += 3
        elif s[idx:idx+3] == "two":
            answer += "2"
            idx += 3
        elif s[idx:idx+5] == "three":
            answer += "3"
            idx += 5
        elif s[idx:idx+4] == "four":
            answer += "4"
            idx += 4
        elif s[idx:idx+4] == "five":
            answer += "5"
            idx += 4
        elif s[idx:idx+3] == "six":
            answer += "6"
            idx += 3
        elif s[idx:idx+5] == "seven":
            answer += "7"
            idx += 5
        elif s[idx:idx+5] == "eight":
            answer += "8"
            idx += 5
        elif s[idx:idx+4] == "nine":
            answer += "9"
            idx += 4
        
    return int(answer)
