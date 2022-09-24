# Merge two sorted linked lists and return it as a new list. 

# The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

# For example, given following linked lists :
#   5 -> 8 -> 20 
#   4 -> 11 -> 15
# The merged list should be :
# 4 -> 5 -> 8 -> 11 -> 15 -> 20

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A.val < B.val:
            head = A
            A = A.next

        else:
            head = B
            B = B.next

        temp = head

        while A and B:
            if A.val < B.val:
                temp.next = A
                A = A.next
            
            else:
                temp.next = B
                B = B.next
            
            temp = temp.next
        
        if A:
            temp.next = A
        
        if B:
            temp.next =  B
            
        return head