#
# @lc app=leetcode id=1480 lang=python
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = nums[0]
        for i in range(1,len(nums)):
            sum += nums[i]
            nums[i] = sum
        
        return nums
    
# @lc code=end

