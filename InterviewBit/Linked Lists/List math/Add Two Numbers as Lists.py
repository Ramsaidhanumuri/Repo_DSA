# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#     342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        tempHead = ListNode(0)
        curr = tempHead
        carry = 0
        
        while A != None or B != None or carry != 0:
            if A:
                val1 = A.val
            
            else:
                val1 = 0
            
            if B:
                val2 = B.val
            
            else:
                val2 = 0
                
            Sum = val1 + val2 + carry
            carry = Sum//10
            Sum = Sum%10
            
            curr.next = ListNode(Sum)
            curr = curr.next
            
            if A:
                A = A.next
            
            else:
                A = None
            
            if B:
                B = B.next
            
            else:
                B = None
        
        return tempHead.next