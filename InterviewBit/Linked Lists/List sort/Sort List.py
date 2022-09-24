# Sort a linked list in O(n log n) time using constant space complexity.

# Example :
# Input : 1 -> 5 -> 4 -> 3
# Returned list : 1 -> 3 -> 4 -> 5

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
import sys
sys.setrecursionlimit(10**5)

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def sortList(self, A):
        if A == None or A.next == None:
            return A
        
        mid = self.midLL(A)
        h1 = A
        h2 = mid.next
        mid.next = None
        
        
        h1 = self.sortList(h1)
        h2 = self.sortList(h2)
        
        return self.mergeTwoLists(h1, h2)
    
    def midLL(self, head):
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow

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