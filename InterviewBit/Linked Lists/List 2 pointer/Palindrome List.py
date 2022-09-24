# Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

# Notes:
# Expected solution is linear in time and constant in space.
# For example,

# List 1-->2-->1 is a palindrome.
# List 1-->2-->3 is not a palindrome.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
    def lPalin(self, A):
        slow = A
        fast = A
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        left = A
        right = prev
        
        while right:
            if left.val != right.val:
                return 0
            left = left.next
            right = right.next
        
        return 1