# greedy approach + sort
# Make a locally optimal decision at each step (merge or not).
# This eventually leads to a globally correct merged result.

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        
        merged = []
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    
    
#     Sort the intervals by start time.

#     Iterate through each interval and decide:

#         If it overlaps → greedily extend the current interval.

#         Else → start a new interval.

# This ensures you're always keeping the least number of merged intervals possible.

# Characteristics of Greedy:

#     Makes immediate decisions.

#     No backtracking.

#     No recursion.

#     No dynamic programming.

#     Works only when the problem has the greedy-choice property (which this one does).