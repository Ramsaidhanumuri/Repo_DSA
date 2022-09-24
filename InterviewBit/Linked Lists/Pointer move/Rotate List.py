# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def rotateRight(self, A, B):
        size = A
        cnt = 1
        while size.next:
            cnt += 1
            size = size.next
        
        B = B%cnt
        if B == 0:
            return A
               
        curr = A
        for i in range(cnt-B-1):
            curr = curr.next
        
        head = curr.next
        curr.next = None
        size.next = A
        
        return head