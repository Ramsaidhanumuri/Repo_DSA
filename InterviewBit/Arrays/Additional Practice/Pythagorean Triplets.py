# A Pythagorean triplet is a set of three integers a, b and c such that a2 + b2 = c2.
# Find the number of pythagorean triplets such that all the elements of the triplet are less than or equal to A.

# Problem Constraints
# 1 <= A <= 103

# Input Format
# Given an integer A.

# Output Format
# Return an integer.

# Example Input
# Input 1:
# A = 5
# Input 2:
# A = 13

# Example Output
# Output 1:
# 1
# Output 2:
# 3

# Example Explanation
# Explanation 1:
# Then only triplet is {3, 4, 5}
# Explanation 2:
# The triplets are {3, 4, 5}, {6, 8, 10}, {5, 12, 13}.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        cnt = 0
        arr = []
        
        for i in range(1,A+1):
            arr.append(i*i)
        
        for i in range(A-1, 1, -1):
            hs = set()
            for j in range(i-1, -1, -1):
                if (arr[i] - arr[j]) in hs:
                    cnt += 1
                hs.add(arr[j])
        
        return cnt