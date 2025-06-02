class Solution(object):
    def maxSubArray(self, nums):
    
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # extend or start new
            max_sum = max(max_sum, current_sum)        # update global max

        return max_sum

#nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
