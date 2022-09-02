# Given a 2D integer matrix A of size N x N find a B x B submatrix where B<= N and B>= 1, such that sum of all the elements in submatrix is maximum.

# Problem Constraints
# 1 <= N <= 103.
# 1 <= B <= N 
# -102 <= A[i][j] <= 102.

# Input Format
# First arguement is an 2D integer matrix A.
# Second argument is an integer B.

# Output Format
# Return a single integer denoting the maximum sum of submatrix of size B x B.

# Example Input
# Input 1:
#  A = [
#         [1, 1, 1, 1, 1]
#         [2, 2, 2, 2, 2]
#         [3, 8, 6, 7, 3]
#         [4, 4, 4, 4, 4]
#         [5, 5, 5, 5, 5]
#      ]
#  B = 3
# Input 2:
#  A = [
#         [2, 2]
#         [2, 2]
#     ]
#  B = 2

# Example Output
# Output 1:
#  48
# Output 2:
#  8

# Example Explanation
# Explanation 1:
#     Maximum sum 3 x 3 matrix is
#     8 6 7
#     4 4 4
#     5 5 5
#     Sum = 48
# Explanation 2:
#  Maximum sum 2 x 2 matrix is
#   2 2
#   2 2
#   Sum = 8

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        M = len(A[0])
        P = [[0]*M for i in range(N)]

        for i in range(N):
            for j in range(M):
                if i == 0:
                    P[i][j] = P[i][j-1] + A[i][j]
                
                elif j == 0:
                    P[i][j] = P[i-1][j] + A[i][j]
                
                else:
                    P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + A[i][j]
            
        ans=float('-inf')
        curr = 0

        for i in range(N):
            for j in range(N):
                if (i+B-1<N and j+B-1<N):
                    x=i+B-1
                    y=j+B-1
                
                    if i == 0 and j == 0:
                        curr = P[x][y]
                    
                    elif i == 0 and j != 0:
                        curr = P[x][y] - P[x][j-1]
                    
                    elif i != 0 and j == 0:
                        curr = P[x][y] - P[i-1][y]

                    else:
                        curr = P[x][y] - P[i-1][y] - P[x][j-1] + P[i-1][j-1]
                    
                    ans = max(ans, curr)
            
        return ans