#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        str_X = str(x)
        new_X = str_X[::-1]

        if new_X == str_X:
            return True
        else:
            return False
        
# @lc code=end

