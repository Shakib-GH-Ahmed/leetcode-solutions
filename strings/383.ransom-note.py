#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash = {}
        for char in magazine:
            hash[char] = hash.get(char,0) + 1

        for item in ransomNote:
            if item not in hash or hash[item] == 0:
                return False
            hash[item] -= 1
        
        return True
        
# @lc code=end

