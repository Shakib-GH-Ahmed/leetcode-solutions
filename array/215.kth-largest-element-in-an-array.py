#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        k = len(nums) - k

        def quickselect(l, r):
            pivot= random.randint(l,r)
            nums[pivot] , nums[r] = nums[r], nums[pivot]
            pivot = nums[r]

            p, q = l, r
            i = l

            while i <= q:
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[q], nums[i] = nums[i], nums[q] 
                    q -= 1

                else:
                    i += 1
                

            if p > k:
                return quickselect(l, p - 1)
            
            elif q < k:
                return quickselect(q + 1, r)
            
            else:
                return pivot

        return quickselect(0, len(nums) - 1)
    
# @lc code=end

