# Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

# Input Format:
# The first and the only argument contains an integer, A.
# Output Format:
# Return a 2-d matrix of size A x A satisfying the spiral order.
# Constraints:

# 1 <= A <= 1000
# Examples:
# Input 1:
#     A = 3

# Output 1:
#     [   [ 1, 2, 3 ],
#         [ 8, 9, 4 ],
#         [ 7, 6, 5 ]   ]

# Input 2:
#     4
# Output 2:
#     [   [1, 2, 3, 4],
#         [12, 13, 14, 5],
#         [11, 16, 15, 6],
#         [10, 9, 8, 7]   ]

class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, A):
        ans = [[0]*A for i in range(A)]
        l = 0
        r = A-1
        t = 0
        d = A-1
        cnt = 1
        D = 0
        
        while l <= r and t <= d:
            if D == 0:
                for i in range(l, r+1):
                    ans[t][i] = cnt
                    cnt += 1
                t += 1
            
            elif D == 1:
                for i in range(t, d+1):
                    ans[i][r] = cnt
                    cnt += 1
                r -= 1
            
            elif D == 2:
                for i in range(r, l-1, -1):
                    ans[d][i] = cnt
                    cnt += 1
                d -= 1
            
            elif D == 3:
                for i in range(d, t-1, -1):
                    ans[i][l] = cnt
                    cnt += 1
                l += 1
            
            D = (D+1)%4
        
        return ans
        