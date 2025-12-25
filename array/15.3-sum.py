#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        j = i + 1
        k = len(nums) - 1
        output = []
        nums.sort()
        
        while i < len(nums) - 2:
            if j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    if [nums[i],nums[j],nums[k]] not in output:
                        output += [[nums[i],nums[j],nums[k]]]

                    j += 1
                    k -= 1

            else:
                i += 1
                if i == len(nums) - 2:
                    break
                j = i + 1
                k = len(nums) - 1

        return output

            
# @lc code=end

