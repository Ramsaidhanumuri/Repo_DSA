# Given an index k, return the kth row of the Pascal's triangle.
# Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

# Example:
# Input : k = 3

# Return : [1,3,3,1]
# Note: k is 0 based. k = 0, corresponds to the row [1]. 

# Note: Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        ans = [[1]]
        
        for i in range(A):
            temp = [0] + ans[-1] + [0]
            row = []
            for j in range(len(ans[-1])+1):
                curr = temp[j] + temp[j+1]
                row.append(curr)
            
            ans.append(row)
        
        return ans[A]