# Reverse a linked list. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL,
# return 5->4->3->2->1->NULL.

# PROBLEM APPROACH :
# Complete solution code in the hints

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def reverseList(self, A):
        if A.next is None:
            return A
        prev = None
        curr = A
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev