#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = 1
        right = 1
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n

        for i in range(n):
            j = - i - 1
            prefix[i] = left
            postfix[j] = right
            left *= nums[i]
            right *= nums[j]

        answer = [0] * n
        for i in range(n):
            answer[i] = prefix[i] * postfix[i]
        
        return answer
           
        
# @lc code=end