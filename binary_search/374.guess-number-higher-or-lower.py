#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n

        while l < r:
            m = l + ((r-l) // 2)
            result = guess(m)
            if result == 1:
                l = m + 1
            elif result == -1:
                r = m - 1
            else:
                return m
        
        return l
            

        
# @lc code=end

