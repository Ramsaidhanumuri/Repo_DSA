# Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.
# Example:

# Input:
# 1 2 3
# 4 5 6
# 7 8 9
# Return the following:
# [ 
#   [1],
#   [2, 4],
#   [3, 5, 7],
#   [6, 8],
#   [9]
# ]

# Input: 
# 1 2
# 3 4
# Return the following: 
# [
#   [1],
#   [2, 3],
#   [4]
# ]

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A)
        N = (2*n)-1
        ans = [list() for i in range(N)]
        
        for i in range(n):
            for j in range(n):
                ans[i+j].append(A[i][j])
        
        return ans