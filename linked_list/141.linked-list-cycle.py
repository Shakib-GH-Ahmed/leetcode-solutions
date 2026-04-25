#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        
        jump1=jump2=head

        while jump2 and jump2.next is not None:
            jump2 = jump2.next.next
            jump1 = jump1.next
            if jump2 == jump1:
                return True
        
        return False

# @lc code=end