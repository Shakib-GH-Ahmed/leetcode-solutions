#
# @lc app=leetcode id=448 lang=python
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = []

        for i in range(len(nums)):
            currentNum = nums[i]
            if currentNum < 0:
                currentNum = -(currentNum)
            
            idx = currentNum - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        for i in range(len(nums)):
            if nums[i] > 0:
                missing.append(i+1)

        return missing
        
# @lc code=end

