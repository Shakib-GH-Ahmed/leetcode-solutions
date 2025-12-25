#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums, 0 , len(nums)-1)
    
    def quicksort(self, nums, l, h):
      if l < h:
        j = self.partition(nums,l,h)
        self.quicksort(nums, l, j-1)
        self.quicksort(nums, j+1, h)

    def partition(self, nums, l , h):
        pivot = nums[l]
        i, j = l, h

        while True:
            while i <= h and nums[i] <= pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            
            if i < j:
                nums[i], nums[j] = nums[j], nums[i] 
            else:
                break
            
        nums[l], nums[j] = nums[j], nums[l]
        return j

        
# @lc code=end

