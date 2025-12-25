#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # for i in range(len(nums) + 1):
        #     if i not in nums:
        #         return i

        sum = 0
        actual_sum = (len(nums) * (len(nums) +1)) / 2

        for i in range(len(nums)):
            sum += nums[i]

        missing_num = actual_sum - sum

        return missing_num
        

        
# @lc code=end

