# Given a singly linked list and an integer K, reverses the nodes of the
# list K at a time and returns modified linked list.

# NOTE : The length of the list is divisible by K
# Example :
# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
# You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
# Try to solve the problem using constant extra space.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def reverseList(self, A, B):
        dummy = ListNode(0)
        dummy.next = A
        groupPrev = dummy
        
        while True:
            kth = self.KthRev(groupPrev, B)
            if not kth:
                break
            groupNxt = kth.next
            
            prev, curr = kth.next, groupPrev.next
            
            while curr != groupNxt:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next
            
    def KthRev(self, curr, K):
        while curr and K > 0:
            curr = curr.next
            K -= 1
        return curr