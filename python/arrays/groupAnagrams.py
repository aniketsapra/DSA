#hashing Map/Set

words = ['bat', 'tab', 'cat', 'tac', 'act']

def groupAnagrams(words):
    map = {}
    
    for word in words:
        key = ''.join(sorted(word)) #sorted word then joined it back into a string
        if key in map:
            map[key].append(word) #if key already exist, append word to the list
        else:
            map[key] = [word]  #if key doesn't exist, make new key
            
    return list(map.values()) #return all values in the map
    
print(groupAnagrams(words))



class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in map:
                map[sorted_word] = []
            map[sorted_word].append(word)
        return list(map.values())