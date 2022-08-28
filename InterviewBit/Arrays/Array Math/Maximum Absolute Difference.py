# You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

# For example,
# A=[1, 3, -1]

# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

# So, we return 5.

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        xmax = float('-inf')
        xmin = float('inf')
        
        ymax = float('-inf')
        ymin = float('inf')
        
        ans = 0
        
        for i in range(len(A)):
            x = A[i] - i
            y = A[i] + i
            
            xmax = max(x, xmax)
            xmin = min(x, xmin)
            
            ymax = max(y, ymax)
            ymin = min(y, ymin)
        
        ans = max(xmax-xmin, ymax-ymin)
        
        return ans