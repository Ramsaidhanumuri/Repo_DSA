# You are given a 2D string array A of dimensions N x 2,
# where each row consists of two strings: first is the name of the student, second is their marks.
# You have to find the maximum average mark. If it is a floating point, round it down to the nearest integer less than or equal to the number.

# Problem Constraints
# 1 <= N <= 105

# Input Format
# The first argument is a 2D string array A.

# Output Format
# Return a single integer which is the highest average mark.

# Example Input
# Input 1:
# A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"]]
# Input 2:
# A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"], ["Alice", "10"]]

# Example Output
# Output 1:
# 90
# Output 2:
# 85

# Example Explanation
# Explanation 1:
# Alice has the highest average with 90 marks.
# Explanation 2:
# Bob has the highest average with 85 marks.

class Solution:
    # @param A : list of list of strings
    # @return an integer
    def highestScore(self, A):
        hm_marks = {}
        hm_cnt = {}
        max_avg = float('-inf')
        
        for name, marks in A:
            if name in hm_marks:
                hm_marks[name] += int(marks)
                hm_cnt[name] += 1
            
            else:
                hm_marks[name] = int(marks)
                hm_cnt[name] = 1
        
        for key, val in hm_marks.items():
            avg = val//hm_cnt[key]
            max_avg = max(max_avg, avg)
        
        return max_avg