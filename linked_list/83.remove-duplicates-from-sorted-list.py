#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = head
        while node and node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
            
        return head


        
# @lc code=end

