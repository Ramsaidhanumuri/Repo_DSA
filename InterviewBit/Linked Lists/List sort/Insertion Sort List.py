# Sort a linked list using insertion sort.
# We have explained Insertion Sort at Slide 7 of Arrays
# Insertion Sort Wiki has some details on Insertion Sort as well.

# Example :
# Input : 1 -> 3 -> 2
# Return 1 -> 2 -> 3

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def insertionSortList(self, A):
        if A.next is None:
            return A
            
        start = ListNode(None)
        start.next = A
        curr = A
        prev = start
        
        while curr:
            if curr.next and curr.val > curr.next.val:
                while prev.next is not None and prev.next.val < curr.next.val:
                    prev = prev.next
                
                temp = prev.next
                prev.next = curr.next
                curr.next = curr.next.next
                prev.next.next = temp
                prev = start
                
            else:
                curr = curr.next
        
        return start.next