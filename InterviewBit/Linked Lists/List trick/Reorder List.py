# Given a singly linked list
#     L: L0 → L1 → … → Ln-1 → Ln,
# reorder it to:
#     L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
# You must do this in-place without altering the nodes’ values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def reorderList(self, A):
        slow = A
        fast = A.next
        
        while fast and fast.next:
            slow = slow.next
            fast =fast.next.next 
        
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        first = A
        second = prev
        
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
        return A