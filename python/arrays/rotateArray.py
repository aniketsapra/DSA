class Solution(object):
    def rotate(self, nums, k):
       
        n = len(nums)
        k = k % n           # Ensure k is within bounds (handle large k)
    
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        
        return nums
    
    
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
