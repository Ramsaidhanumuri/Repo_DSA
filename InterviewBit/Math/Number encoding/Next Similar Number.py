# Given a number A in a form of string.
# You have to find the smallest number that has same set of digits as A and is greater than A.
# If A is the greatest possible number with its set of digits, then return -1.

# Problem Constraints
#  1 <= A <= 10100000
#  A doesn't contain leading zeroes.

# Input Format
# First and only argument is an numeric string denoting the number A.

# Output Format
# Return a string denoting the smallest number greater than A with same set of digits , if A is the largest possible then return -1.

# Example Input
# Input 1:
#  A = "218765"
# Input 2:
#  A = "4321"

# Example Output
# Output 1:
#  "251678"
# Output 2:
#  "-1"

# Example Explanation
# Explanation 1:
#  The smallest number greater then 218765 with same set of digits is 251678.
# Explanation 2:
#  The given number is the largest possible number with given set of digits so we will return -1.

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        B = []
        for i in A:
            B.append(int(i))
            
        n = len(B)

        if n <= 1:
            return -1

        i = n - 1

        while i > 0 and B[i] <= B[i - 1]:
            i -= 1
        if i > 0:
            j = n - 1
            while j >= i:
                if B[j] > B[i - 1]:
                    B[j], B[i - 1] = B[i - 1], B[j]
                    break
                j -= 1

        m = n - 1
        while i < m:
            B[i], B[m] = B[m], B[i]
            i += 1
            m -= 1

        ans = ''
        for i in B:
            ans += str(i)
        
        if int(ans) > int(A):
            return ans
        
        return -1