#
# @lc app=leetcode id=2215 lang=python
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        lst = []
        
        for i in nums1:
            if i not in nums2:
                lst.append(i)         
            else:
                nums2.remove(i)

        nums2 = list(nums2)

        return [lst,nums2]

        
# @lc code=end