#
# @lc app=leetcode id=876 lang=python
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        jump1=jump2=head

        while jump2 and jump2.next is not None:
            jump2 = jump2.next.next
            jump1 = jump1.next
            
        return jump1   
    
# @lc code=end