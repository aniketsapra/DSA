#hashing Map/Set

string = 'aabbcde'

def firstUniqueChar(string):
    map = {}
    
    for ch in string:
        map[ch] = map.get(ch, 0) + 1
        
    for ch in string:
        if map[ch] == 1:
            return ch
            
    return None
    
print(firstUniqueChar(string))