class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        currSum = 0
        prefixSums = {0:1}

        for num in nums:
            currSum += num
            if (currSum - k) in prefixSums:
                count += prefixSums[currSum - k]
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
        
        return count

