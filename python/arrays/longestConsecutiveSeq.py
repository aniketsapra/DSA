class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
            
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest = max(longest, current_streak)
        
        return longest
    
    
class Solution(object):
    def longestConsecutive(self, nums):
        longest=0
        numset=set(nums)
        for num  in numset:
            length=1
            if num-1 not in numset:
                while (num+length) in numset:
                    length+=1
                longest=max(length,longest)
        return longest




        # for i in numset:
        #     num= list(row[i])[0]
            
        #     count=0
        #     if num-1 in row:
        #         count+=1
            
        #     else:
        #         continue

        # return count