#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashT = {}
        
        for i in range(len(nums)):
            if nums[i] not in hashT:
                hashT[nums[i]] = i
            else:
                return True
            
        return False
        
# @lc code=end

