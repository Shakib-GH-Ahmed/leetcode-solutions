#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        stack = [(root.left, root.right)]

        while stack:
            l,r = stack.pop()
            if l is None and r is None:
                continue
            if l is None or r is None or l.val != r.val:
                return False
            
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))

        return True
        
# @lc code=end

