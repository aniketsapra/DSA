class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# we start with i making it second last (n-2) 
# then finding decreasing element 
# Find i where nums[i] < nums[i+1]
#     nums[3] = 4, nums[4] = 2 → 4 >= 2 → i = 2
#     nums[2] = 5, nums[3] = 4 → 5 >= 4 → i = 1
#     nums[1] = 3, nums[2] = 5 → 3 < 5 → stop here
#     i = 1
    
# Find j where nums[j] > nums[i]
# j = len(nums) - 1 = 4 (last element)
# nums[4] = 2 → 2 <= 3 → j = 3
# nums[3] = 4 → 4 > 3 → stop here
# j = 3

# Swap nums[i] and nums[j]
# Before swap: [1, 3, 5, 4, 2]
# Swap nums[1] and nums[3]: 3 <-> 4
# After swap:  [1, 4, 5, 3, 2]

# Reverse the subarray from i + 1 to end
# We now reverse from i + 1 = 2 to end (left = 2, right = 4):
# Swap nums[2] and nums[4] → 5 <-> 2
# Array: [1, 4, 2, 3, 5]
# left = 3, right = 3 → done