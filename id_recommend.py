import re

def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    
    new_id = re.sub(r"[^a-z0-9\-\_\.]", "", new_id)
    new_id = re.sub(r"\.+", ".", new_id)
    new_id = re.sub(r"^\.|\.$", "", new_id)
    if new_id == "":
        new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[:15]
    new_id = re.sub(r"^\.|\.$", "", new_id)
    if len(new_id) < 3:
        for i in range(3-len(new_id)):
            new_id += new_id[-1]
    
    answer = new_id
    
    return answer
