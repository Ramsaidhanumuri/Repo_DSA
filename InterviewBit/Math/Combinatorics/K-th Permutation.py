# You are given an integer A which represents the length of a permutation.
#  A permutation is an array of length A where all the elements occur exactly once and in any order.
#  For example, [3, 4, 1, 2], [1, 2, 3] are examples of valid permutations while [1, 2, 2], [2] are not.

# You are also given an integer B.
#  If all the permutation of length A are sorted lexicographically, return the Bth permutation.

# Problem Constraints
# 1 <= A <= 105
# 1 <= B <= min(1018, A!), where A! denotes the factorial of A.

# Input Format
# The first argument is the integer A.
# The second argument is the long integer B.

# Output Format
# Return an array denoting the Bth permutation of length A.

# Example Input
# Input 1:
# A = 3
# B = 3
# Input 2:
# A = 1
# B = 1

# Example Output
# Output 1:
# [2, 1, 3]
# Output 2:
# [1]

# Example Explanation
# Explanation 1:
# All the permutations of length 3 sorted in lexicographical order are:
# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
# Therefore, the third permutation is [2, 1, 3].
# Explanation 2:
# There is only one possible permutation -> [1].

class Solution:
    # @param A : integer
    # @param B : long
    # @return a list of integers
    def findPerm(self, A, B):
        fact = [0]*21
        fact[0] = 1
        for i in range(1, 21):
            fact[i] = i * fact[i - 1]
        
        ans = [0]*A
        curr = 0
        for i in range(A-20):
            ans[i] = i + 1
            curr = i
        
        l1 = []
        for i in range(max(A - 20, 1), A+1):
            l1.append(i)
        B-=1
        
        for i in range(min(20, A - 1), -1, -1): 
            idx = (B // fact[i])
            B -= idx * fact[i]
            ans[curr] = l1[idx]
            curr+=1
            l1.pop(idx)
        
        return ans