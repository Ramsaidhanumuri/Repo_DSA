# Given a number N, find all factors of N.

# Example:
# N = 6 
# factors = {1, 2, 3, 6}
# Make sure the returned array is sorted.

from math import sqrt
class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        
        L=[]
        for i in range(1,int(sqrt(A))+1):
            if(A%i==0):
                L.append(int(i))
                if(i!=sqrt(A)):
                    L.append(int(A/i))
        L.sort()
        return(L)