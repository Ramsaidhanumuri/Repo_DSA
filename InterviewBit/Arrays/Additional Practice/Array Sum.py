# You are given two numbers represented as integer arrays A and B, where each digit is an element.
# You have to return an array which representing the sum of the two given numbers.
# The last element denotes the least significant bit, and the first element denotes the most significant bit.

# Problem Constraints
# 1 <= |A|, |B| <= 105
# 0 <= Ai, Bi <= 9

# Input Format
# The first argument is an integer array A. The second argument is an integer array B.

# Output Format
# Return an array denoting the sum of the two numbers.

# Example Input
# Input 1:
# A = [1, 2, 3]
# B = [2, 5, 5]
# Input 2:
# A = [9, 9, 1]
# B = [1, 2, 1]

# Example Output
# Output 1:
# [3, 7, 8]
# Output 2:
# [1, 1, 1, 2]

# Example Explanation
# Explanation 1:
# Simply, add all the digits in their place.
# Explanation 2:
# 991 + 121 = 1112
# Note that the resultant array size might be larger.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def addArrays(self, A, B):
        n = len(A)
        m = len(B)
        if n > m:
            B = [0]*(n-m) + B
            s = n
        else:
            A = [0]*(m-n) + A
            s = m
            
        ans = [0]*s
        carry = 0
        
        for i in range(s-1, -1, -1):
            total = A[i] + B[i] + carry
            
            carry = total//10
            total = total%10
            
            ans[i] = total
        
        if carry == 1:
            return [1] + ans
        
        return ans