# Given a target A on an infinite number line, i.e. -infinity to +infinity.
# You are currently at position 0 and you need to reach the target by moving according to the below rule:

# In ith move you can take i steps forward or backward.
# Find the minimum number of moves required to reach the target.

# Problem Constraints
# -109 <= A <= 109

# Input Format
# First and only argument is an integer A.

# Output Format
# Return an integer denoting the minimum moves to reach target.

# Example Input
# Input 1:
#  3
# Input 2:
#  2

# Example Output
# Output 1:
#  2
# Output 2:
#  3

# Example Explanation
# Explanation 1:
#  On the first move we step from 0 to 1.
#  On the second step we step from 1 to 3.
# Explanation 2:
#  On the first move we step from 0 to 1.
#  On the second move we step  from 1 to -1.
#  On the third move we step from -1 to 2.

import math

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        A = abs(A)
        i = int(math.sqrt(1+8*A)-1)//2
        running_sum = i*(i+1)//2
        
        if running_sum < A:
            i += 1
            running_sum += i
        
        while (running_sum-A)%2 != 0:
            i += 1
            running_sum += i
        
        return i 