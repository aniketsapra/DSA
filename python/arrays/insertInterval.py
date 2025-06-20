class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        merged = []

        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
    