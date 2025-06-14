# Hard Leetcode
# Sliding window

import collections

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, nums, k):
        count = collections.Counter()
        left = 0
        total = 0

        for right in range(len(nums)):
            if count[nums[right]] == 0:
                k -= 1
            count[nums[right]] += 1

            while k < 0:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    k += 1
                left += 1

            total += right - left + 1

        return total