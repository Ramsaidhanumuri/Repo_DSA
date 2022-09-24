# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# return 1->4->3->2->5->NULL.

# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.
# Note 2:
# Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if A.next is None:
            return A
        dummy = ListNode(0)
        dummy.next = A
        leftPrev = dummy
        curr = leftPrev.next
        
        for i in range(B-1):
            leftPrev = curr
            curr = curr.next
        
        prev = None
        for i in range(C-B+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        return dummy.next