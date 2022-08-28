# Note: this solution works in Leetcode but in InterviewBit we get TC

# Given a list of non negative integers, arrange them such that they form the largest number.

# For example:
# Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        n = len(A)
        ans = ''
        A = list(A)
        
        for i in range(n):
            l = i
            r = i + 1
            
            while r < n:
                val1 = int(str(A[l]) + str(A[r]))
                val2 = int(str(A[r]) + str(A[l]))
                
                if val1 > val2:
                    r += 1
                else:
                    A[l], A[r] = A[r], A[l]
                    r += 1
            
            ans += str(A[i])
        if int(ans) == 0:
            return 0
            
        return ans