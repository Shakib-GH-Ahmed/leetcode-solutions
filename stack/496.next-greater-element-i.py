#
# @lc app=leetcode id=496 lang=python
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        output = []
        hashmap = {}

        for i in range(len(nums2)-1,-1,-1):
            curr = nums2[i]

            while stack and stack[-1] <= curr:
                stack.pop()

            if not stack:
                hashmap[curr] = -1
            else:
                hashmap[curr] = stack[-1]
            
            stack.append(curr)
        
        for i in nums1:
            output.append(hashmap[i])
        
        return output
        
# @lc code=end