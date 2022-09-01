# Given numRows, generate the first numRows of Pascal's triangle.
# Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

# Example:
# Given numRows = 5,

# Return
# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]
# Constraints:
# 0 <= numRows <= 25

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        ans = [[1]]
        
        if A==0:
            return []
        
        for i in range(A-1):
            temp = [0] + ans[-1] + [0]
            row = []
            
            for j in range(len(ans[-1])+1):
                curr = temp[j] + temp[j+1]
                row.append(curr)
            
            ans.append(row)
        
        return ans