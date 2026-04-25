#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current != None:
            if current.next != None and current.val == current.next.val: 
                    while current.next != None and current.val == current.next.val:
                            current = current.next
                    
                    prev.next = current.next
                    current = current.next
            else:
                prev = current
                current = current.next

        return dummy.next

 
# @lc code=end