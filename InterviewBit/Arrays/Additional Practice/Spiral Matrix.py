# Given an array of A of length B×C.
# Make a Spiral matrix (2D array) of B rows and C columns.

# Note: See example input for pattern.

# Problem Constraints
# 1 <= Ai <=105
# 1 <= B×C <= 105

# Input Format
# First argument is an integer array A.
# Second argument is an integer B.
# Third argument is an integer C.

# Output Format
# Return 2D integer array.

# Example Input
# Input 1:
# A = [1, 2, 4, 8]
# B = 2
# C = 2
# Input 2:
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# B = 3
# C = 3

# Example Output
# Output 1:
# [[1, 2],
#  [8, 4]]
# Output 2:
# [[1, 2, 3],
#  [8, 9, 4],
#  [7, 6, 5]]

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of list of integers
    def solve(self, A, B, C):
        ans = [[0]*C for i in range(B)]
        t = 0
        d = B-1
        l = 0
        r = C-1
        D = 0
        cnt = 0
        
        while t <= d and l <= r:
            if D == 0:
                for i in range(l, r+1):
                    ans[t][i] = A[cnt]
                    cnt += 1
                t += 1
            
            elif D == 1:
                for i in range(t, d+1):
                    ans[i][r] = A[cnt]
                    cnt += 1
                r -= 1
            
            elif D == 2:
                for i in range(r, l-1, -1):
                    ans[d][i] = A[cnt]
                    cnt += 1
                d -= 1
            
            elif D == 3:
                for i in range(d, t-1, -1):
                    ans[i][l] = A[cnt]
                    cnt += 1
                l += 1
            
            D = (D+1)%4
        
        return ans