#here made a list then sorted the list then joined the list into a string to check

class Solution(object):
    def isAnagram(self, s, t):
        s_list = list(s)
        t_list = list(t)
        
        sorted_s = sorted(s_list)
        sorted_t = sorted(t_list)
        
        s = ''.join(sorted_s)
        t = ''.join(sorted_t)
        
        if s == t:
            return True
        else:
            return False
        
        
#sorted(s) will give sorted list of characters in string s

class Solution(object):
    def isAnagram(self, s, t):
        if sorted(s) == sorted(t):
            return True
        else:
            return False
