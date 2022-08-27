# Given a string A which represents a time in 24 hour HH:MM format.
# Find the minimum number of minutes need to pass to reach palindromic time.
# Let some time be XY:ZW then it is palindromic if X == W and Y == Z.

# Problem Constraints
# String A represents a valid time in HH:MM format.

# Input Format
# Given a string A.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = "23:59"
# Input 2:
# A = "21:00"

# Example Output
# Output 1:
# 1
# Output 2:
# 12

# Example Explanation
# Explanation 1:
# After 1 minute time will be 00:00 which is a palindromic time.
# Explanation 2:
# After 12 minute time will be 21:12 which is a palindromic time.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        h = int(A[0]+A[1])
        m = int(A[3]+A[4])
        
        ans = 0
        
        while h//10 != m%10 or h%10 != m//10:
            m += 1
            
            if m==60:
                m = 0
                h += 1
            
            if h == 24:
                h = 0
            
            ans += 1
        
        return ans