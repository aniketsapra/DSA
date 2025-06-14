# prefix sum
# medium 


from collections import defaultdict

class Solution(object):
    def leastBricks(self, wall):
        count = defaultdict(int)

        for row in wall:
            total = 0
            for brick in row[:-1]:    #[:-1] to exclude last edge
                total += brick
                count[total] += 1
        if count:
            max_edges = max(count.values())
        else:
            max_edges = 0
            
        return len(wall) - max_edges #6-4
    
    
# | Row        | Brick edges (prefix sums) |
# | ---------- | ------------------------- |
# | \[1,2,2,1] | 1, 3, 5                   |
# | \[3,1,2]   | 3, 4                      |
# | \[1,3,2]   | 1, 4                      |
# | \[2,4]     | 2                         |
# | \[3,1,2]   | 3, 4                      |
# | \[1,3,1,1] | 1, 4, 5                   |

# So, we record how often each edge appears (excluding final edge):
# {
#   1: 3 times,
#   2: 1 time,
#   3: 3 times,
#   4: 4 times,
#   5: 2 times
# }

# → The best edge is at position 4, which appears in 4 rows.