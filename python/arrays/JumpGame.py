# Greedy Approach

class Solution(object):
    def canJump(self, nums):
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True
    
# maxReach = max index we can reach
# if we're beyond reach we cannot go further
# greedily update the farthest point we can reach
# if we never hit a 'Stuck' point, we can reach the end
# [2,3,1,1,4] and [3,2,1,0,4] test cases try 
# At index 0, nums[0] = 2.
# So, from index 0, you can jump to:

#     0 + 1 = 1
#     0 + 2 = 2
# Therefore, the farthest you can go from index 0 is 0 + 2 = 2.