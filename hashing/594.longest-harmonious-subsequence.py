#
# @lc app=leetcode id=594 lang=python
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        longest = 0

        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        if len(dict) <= 1:
            return 0
        
        for key,value in dict.items():
            sum = 0
            next = key+1
            if next in dict:
                sum = value + dict[next]
                if sum > longest:
                    longest = sum

        return longest
    
        
# @lc code=end