#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = i + 1
        k = len(nums) - 1

        nums.sort()
        
        closest = float('inf')

        while i < len(nums) - 2:
            if j < k:
                sum = nums[i] + nums[j] + nums[k]

                if abs(target - sum) < abs(target - closest):
                    closest = sum

                if sum > target:
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    return sum

            else:
                i += 1
                if i == len(nums) - 2:
                    break
                j = i + 1
                k = len(nums) - 1

        return closest

        
# @lc code=end

