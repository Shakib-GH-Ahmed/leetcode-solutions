#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words_lst = s.split(" ")
        if len(pattern) != len(words_lst):
            return False

        hash1 = {}  #character to word
        hash2 = {}  #word to character

        for i in range(len(pattern)):
            if words_lst[i] not in hash2:
                if pattern[i] in hash1:
                    return False
                hash1[pattern[i]] = words_lst[i]
                hash2[words_lst[i]] = pattern[i]
                
            else:
                if pattern[i] != hash2[words_lst[i]]:
                    return False
                
        return True

            
        
# @lc code=end

