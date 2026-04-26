#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        single = double = head
        while double and double.next:
            double = double.next.next
            single = single.next
        
        prev = None
        current = single
        while current is not None:
            store = current.next
            current.next = prev
            prev = current
            current = store
        
        node1 = head
        node2 = prev
        while node2 is not None:
            if node1.val == node2.val:
                node1 = node1.next
                node2 = node2.next
            else:
                return False

        return True           
        
# @lc code=end