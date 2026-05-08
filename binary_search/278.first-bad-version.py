#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n

        while l < r:
            m = l + ((r-l) // 2)
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        return r

        
# @lc code=end

