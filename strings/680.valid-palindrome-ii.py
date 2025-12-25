#
# @lc app=leetcode id=680 lang=python
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
                
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPal(l+1, r) or isPal(l, r-1)
 
        return True

# @lc code=end

