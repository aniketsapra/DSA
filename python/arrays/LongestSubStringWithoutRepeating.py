# Longest Substring without Repeating char
# Sliding window with hashSet


string = 'abcabcbb'

def lengthOfLongestSubstringNotRepeating(string):
    my_set = set()
    left = 0 
    maxLen = 0
    for right in range(len(string)):
        while string[right] in my_set:
            my_set.remove(string[left])
            left += 1
        my_set.add(string[right])
        maxLen = max(maxLen, right - left + 1) 
        #used to calculate the length of the current substring (or window) you're evaluating
    return maxLen
    
print(lengthOfLongestSubstringNotRepeating(string)) # Output: 3


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left, maxLen = 0, 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen

# right = 0 → 'a'

#     'a' not in my_set

#     Add 'a' → my_set = {'a'}

#     Update maxLen = max(0, 0 - 0 + 1) = 1

# ▶️ right = 1 → 'b'

#     'b' not in my_set

#     Add 'b' → my_set = {'a', 'b'}

#     Update maxLen = max(1, 1 - 0 + 1) = 2

# ▶️ right = 2 → 'c'

#     'c' not in my_set

#     Add 'c' → my_set = {'a', 'b', 'c'}

#     Update maxLen = max(2, 2 - 0 + 1) = 3

# ▶️ right = 3 → 'a'

#     'a' is in my_set, so:

#         Remove 'a' at left = 0 → my_set = {'b', 'c'}

#         Increment left = 1

#     Now 'a' not in my_set, so:

#         Add 'a' → my_set = {'a', 'b', 'c'}

#     Update maxLen = max(3, 3 - 1 + 1) = 3

# ▶️ right = 4 → 'b'

#     'b' is in my_set

#         Remove 'b' at left = 1 → my_set = {'a', 'c'}

#         Increment left = 2

#     Add 'b' → my_set = {'a', 'b', 'c'}

#     maxLen = max(3, 4 - 2 + 1) = 3

# ▶️ right = 5 → 'c'

#     'c' is in my_set

#         Remove 'c' at left = 2 → my_set = {'a', 'b'}

#         left = 3

#     Add 'c' → my_set = {'a', 'b', 'c'}

#     maxLen = max(3, 5 - 3 + 1) = 3

# ▶️ right = 6 → 'b'

#     'b' is in my_set

#         Remove 'a' at left = 3 → my_set = {'b', 'c'}

#         left = 4

#         Remove 'b' at left = 4 → my_set = {'c'}

#         left = 5

#     Add 'b' → my_set = {'b', 'c'}

#     maxLen = max(3, 6 - 5 + 1) = 3

# ▶️ right = 7 → 'b'

#     'b' is in my_set

#         Remove 'c' at left = 5 → my_set = {'b'}

#         left = 6

#         Remove 'b' at left = 6 → my_set = {}

#         left = 7

#     Add 'b' → my_set = {'b'}

#     maxLen = max(3, 7 - 7 + 1) = 3