class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        minP = maxP = result = nums[0]

        for num in nums[1:]:
            if num < 0:
                minP, maxP = maxP, minP
            
            minP = min(num, minP * num)
            maxP = max(num, maxP * num)
            result = max(result, maxP)
        return result

