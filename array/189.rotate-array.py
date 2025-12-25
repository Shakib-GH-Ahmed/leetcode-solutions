#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new = [0] * len(nums)
        for i in range(len(nums)):
            pos = (i + k) % len(nums)
            new[pos] = nums[i]
        
        nums[:] = new

      
# @lc code=end

