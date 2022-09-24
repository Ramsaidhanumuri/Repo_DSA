# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = ListNode(0)
        head.next = A
        prev = head
        curr = prev.next
        nxt = curr.next
        
        while nxt:
            if curr.val != nxt.val:
                prev = prev.next
                curr = curr.next
                nxt = nxt.next
            
            else:
                while curr != nxt and nxt:
                    nxt = nxt.next
                      
                curr = nxt
                prev.next = curr
                if nxt:
                    nxt = nxt.next
        
        return head.next