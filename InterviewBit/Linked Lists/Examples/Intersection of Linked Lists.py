# Write a program to find the node at which the intersection of two singly linked lists begins.
# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3

# begin to intersect at node c1.

# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
# Problem approach completely explained :

# Complete code in the hints section.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        cnt1 = 0
        cnt2 = 0
        headA = A
        headB = B
        
        while A:
            A = A.next
            cnt1 += 1
        
        while B:
            B = B.next
            cnt2 += 1
            
        A = headA
        B = headB
        
        if cnt1 > cnt2:
            n = cnt1 - cnt2
            for i in range(n):
                A = A.next
        
        else:
            n = cnt2-cnt1
            for i in range(n):
                B = B.next
        
        for i in range(min(cnt1, cnt2)):
            if A == B:
                return A
            
            A = A.next
            B = B.next
        
        return None