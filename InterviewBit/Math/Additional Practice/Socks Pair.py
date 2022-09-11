# Given an integer array A of integers.
# Every element in the array repersent a colour of a sock, find how many pair of socks with matching colours there are.

# Problem Constraints
# 1 <= |A| <= 105
# 1 <= Ai <= |A|

# Input Format
# Given an integer array A.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = [1, 2, 3]
# Input 2:
# A = [2, 2, 2, 2]

# Example Output
# Output 1:
# 0
# Output 2:
# 2

# Example Explanation
# Explanation 1:
# No pair of socks can be formed.
# Explanation 2:
# Two pairs of socks can be formed.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hm = {}
        cnt = 0
        
        for i in A:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
            
            if hm[i]%2==0:
                cnt += 1
            
        return cnt