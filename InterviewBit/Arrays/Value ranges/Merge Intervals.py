# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
# Make sure the returned intervals are also sorted.

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param A, a list of A
    # @param B, a Interval
    # @return a list of Interval
    def insert(self, A, B):
        s = min(B.start, B.end)
        e = max(B.start, B.end)
        n = len(A)
        ans = []
        
        for i in range(n):
            if s <= A[i].end and s >= A[i].start:
                e = max(A[i].end, e)
                s = A[i].start
            
            elif s < A[i].start and e >= A[i].start:
                e = max(A[i].end, e)
            
            elif s < A[i].start and e < A[i].start:
                ans.append(Interval(s, e))
                s = A[i].start
                e = A[i].end
            
            elif s > A[i].end:
                ans.append(A[i])
                
        ans.append(Interval(s, e))  
        
        return ans