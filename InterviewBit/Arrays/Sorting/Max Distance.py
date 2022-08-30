# Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

# Input Format
# First and only argument is an integer array A.

# Output Format
# Return an integer denoting the maximum value of j - i;

# Example Input
# Input 1:
#  A = [3, 5, 4, 2]

# Example Output
# Output 1:
#  2

# Example Explanation
# Explanation 1:
#  Maximum value occurs for pair (3, 4).

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        arr = []
        n = len(A)
        
        for i in range(n):
            arr.append([A[i], i])
        
        arr.sort()
        ans = 0
        max_ind = arr[n-1][1]
        
        for i in range(n-2, -1, -1):
            ans = max(ans, max_ind - arr[i][1])
            max_ind = max(max_ind, arr[i][1])
        
        
        return ans