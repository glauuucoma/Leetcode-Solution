#Author: Davyd Kuleba
#Year: 2023
#Description: My solutions to popular LeetCode problems.

#876. Middle of The Linked List
#Two pointers method

#Space complexity O(n)
#Time complexity O(n)

"""
Two pointers method creates
fast and slow pointers, fast one is one step ahead of the slow one,
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        slow,fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


