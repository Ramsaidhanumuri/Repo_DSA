# Given a collection of intervals, merge all overlapping intervals.

# For example:
# Given [1,3],[2,6],[8,10],[15,18],

# return [1,6],[8,10],[15,18].
# Make sure the returned intervals are sorted.

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key = lambda i : i.start )
        ans = [intervals[0]]
        
        for i in intervals[1:]:
            lastEnd = ans[-1].end
            
            if i.start <= lastEnd:
                ans[-1].end = max(i.end, lastEnd)
            
            else:
                ans.append((i))
        
        return ans