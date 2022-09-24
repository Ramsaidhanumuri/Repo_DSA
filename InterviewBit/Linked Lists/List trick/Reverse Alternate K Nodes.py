# Given a linked list A of length N and an integer B.
# You need to reverse every alternate B nodes in the linked list A.

# Problem Constraints
# 1 <= N <= 105
# 1<= Value in Each Link List Node <= 103
# 1 <= B <= N
# N is divisible by B

# Input Format
# First argument is the head pointer of the linkedlist A.
# Second argument is an integer B.

# Output Format
# Return the head pointer of the final linkedlist as described.

# Example Input
# Input 1:
#  A = 3 -> 4 -> 7 -> 5 -> 6 -> 6 -> 15 -> 61 -> 16
#  B = 3
#  Input 2:
#  A = 1 -> 4 -> 6 -> 6 -> 4 -> 10
#  B = 2

# Example Output
# Output 1:
#  7 -> 4 -> 3 -> 5 -> 6 -> 6 -> 16 -> 61 -> 15
# Output 2:
#  4 -> 1 -> 6 -> 6 -> 10 -> 4

# Example Explanation
# Explanation 1:
#  The linked list contains 9 nodes and we need to reverse alternate 3 nodes.
#  First sublist of length 3  is 3 -> 4 -> 7 so on reversing it we get 7 -> 4 -> 3.
#  Second sublist of length 3 is 5 -> 6 -> 6 we don't need to reverse it.
#  Third sublist of length 3 is 15 -> 61 -> 16 so on reversing it we get 16 -> 61 -> 15.
# Explanation 2:
#  The linked list contains 6 nodes and we need to reverse alternate 2 nodes.
#  First sublist of length 2 is 1 -> 4 so on reversing it we get 4 -> 1.
#  Second sublist of length 2 is 6 -> 6 we don't need to reverse it.
#  Third sublist of length 2 is 4 -> 10 so on reversing it we get 10 -> 4.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        prev = None
        curr = A
        
        while curr:
            last = curr
            first, curr = self.reverseLL(curr, B)
            
            if prev is None:
                A = first
            
            else:
                prev.next = first
            
            last.next = curr
            prev, curr = self.skipNodes(curr, B)
        
        return A
    
    def reverseLL(self, curr, B):
        prev = None
        
        while curr and B >0:
            B = B - 1
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev, curr
    
    def skipNodes(self, curr, B):
        prev = None
        
        while curr and B > 0:
            B = B - 1
            prev = curr
            curr = curr.next
        
        return prev, curr