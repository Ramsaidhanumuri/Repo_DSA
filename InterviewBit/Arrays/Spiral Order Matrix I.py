# Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example:
# Given the following matrix:
# [
#     [ 1, 2, 3 ],
#     [ 4, 5, 6 ],
#     [ 7, 8, 9 ]
# ]
# You should return
# [1, 2, 3, 6, 9, 8, 7, 4, 5]

class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
        n = len(A)
        m = len(A[0])
        ans = [0]*(m*n)
        l = 0
        r = m - 1
        t = 0
        d = n-1
        cnt = 0
        D = 0
        
        while l <= r and t <= d:
            if D == 0:
                for i in range(l, r+1):
                    ans[cnt] = A[t][i]
                    cnt += 1
                t += 1
            
            elif D == 1:
                for i in range(t, d+1):
                    ans[cnt] = A[i][r]
                    cnt += 1
                r -= 1
            
            elif D == 2:
                for i in range(r, l-1, -1):
                    ans[cnt] = A[d][i]
                    cnt += 1
                d -= 1
            
            elif D == 3:
                for i in range(d, t-1, -1):
                    ans[cnt] = A[i][l]
                    cnt += 1
                l += 1
            
            D = (D+1)%4
            
        return ans