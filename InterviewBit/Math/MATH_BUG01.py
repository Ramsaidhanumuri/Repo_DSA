# Following code tries to figure out if a number is prime ( Wiki )

# However, it has a bug in it.

# Please correct the bug and then submit the code.

class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A > 1:
            for i in range(2, A):
                if A % i == 0:
                    return 0
            return 1
        return 0
