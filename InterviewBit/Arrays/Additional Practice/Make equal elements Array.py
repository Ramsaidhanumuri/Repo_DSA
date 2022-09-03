# Given an array of all positive integers and an element “x”. 
# You need to find out whether all array elements can be made equal or not by performing any of the 3 operations: add x to any element in array, subtract x from any element from array, do nothing.

# This operation can be performed only once on an element of array.

# Problem Constraints
# 1<=|A|<=1e5
# 1<=A[i],x<=1e9

# Input Format
# First argument is array of integers .
# Second argument is B which denotes the value of x.

# Output Format
# Return 1 if we can make all elements equal , otherwise return 0.

# Example Input
# Input 1:
# A=[2,3,1]
# X=1
# Input 2:
# A=[2,3,1]
# X=2

# Example Output
# Ouput 1:
# 1
# Ouput 2:
# 0

# Example Explanation
# Explanation 1:
# WE can make all elements equal to 2.
# Explanation 2:
# There is no way to make all elements equal to 0.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_val = max(A)-B
        min_val = min(A)+B
        
        if min_val != max_val:
            return 0
                   
        return 1