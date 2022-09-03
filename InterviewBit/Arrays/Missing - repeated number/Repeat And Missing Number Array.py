# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.

# Return A and B.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Note that in your output A should precede B.

# Example:
# Input:[3 1 2 5 3] 

# Output:[3, 4] 
# A = 3, B = 4

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        hm = {}
        R = 0
        M = 0
        
        for i in A:
            if i in hm:
                hm[i] += 1
                
                if hm[i]>1:
                     R = i
            
            else:
                hm[i] = 1
                
        cnt = 1
        for key, val in hm.items():
            if cnt == key:
                cnt += 1
            
            else:
                M = cnt
                break
        if M == 0:
            M = len(hm)+1
        return [R, M]