#Hashing Map/Set

string = "abca"

def firstNonRepeatingChar(string):
    map = {}
    for ch in string:
        map[ch] = map.get(ch,0) + 1 #if ch not found make it zero and then add 1
        
    for i in range(len(string)):
        if map.get(string[i]) == 1:
            return string[i]
            
    return "there is no Non-Repeating Character"

print(firstNonRepeatingChar(string))



#Char Frequecy Count

string = 'aniketsapra'

def charFrequency(string):
    map = {}
    for ch in string:
        map[ch] = map.get(ch,0) + 1
    return map
    
print(charFrequency(string))

#{'a': 3, 'n': 1, 'i': 1, 'k': 1, 'e': 1, 't': 1, 's': 1, 'p': 1, 'r': 1}