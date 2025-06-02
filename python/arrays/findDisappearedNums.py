class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


#better and easy approach
 
class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        set_nums = set(nums)

        ret = []

        for i in range(1,len(nums)+1):
            if i not in set_nums:
                ret.append(i)

        return ret
