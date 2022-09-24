# Given a linked list A , reverse the order of all nodes at even positions.

# Problem Constraints
# 1 <= Size of linked list <= 100000

# Input Format
# First and only argument is the head of the Linked-List A.

# Output Format
# Return the head of the new linked list.

# Example Input
# Input 1:
# A = 1 -> 2 -> 3 -> 4
# Input 2:
# A = 1 -> 2 -> 3

# Example Output
# Output 1:
#  1 -> 4 -> 3 -> 2
# Output 2:
#  1 -> 2 -> 3

# Example Explanation
# Explanation 1:
# Nodes are positions 2 and 4 have been swapped.
# Explanation 2:
# No swapping neccassary here.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        even = None
        odd = A
        
        if (odd == None or odd.next == None or odd.next.next == None):
            return odd
    
        while (odd and odd.next):
            temp = odd.next
            odd.next = temp.next
            temp.next = even
            even = temp
            odd = odd.next
    
        odd = A
        
        while (even):
            temp = even.next
            even.next = odd.next
            odd.next = even
            even = temp
            odd = odd.next.next
        return A