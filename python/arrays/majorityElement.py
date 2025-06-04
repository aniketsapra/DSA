class Solution(object):
    def majorityElement(self, nums):
        count_map = {}
    
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        # The majority element appears more than n//2 times
        majority_count = len(nums) // 2

        for num, count in count_map.items():
            if count > majority_count:
                return num
            


nums = [3,2,3]
def majorityElement(nums):
        map = {}
        maxocc = 0
        for num in nums:
            map[num] = map.get(num, 0) + 1
            
        for num, value in map.items():
            maxocc = max(maxocc, value)
        
        for num, value in map.items():
            if value == maxocc:
                return num
        
print(majorityElement(nums))