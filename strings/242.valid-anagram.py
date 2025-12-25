#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dictS, dictT = {}, {}

        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)
        
        #print(dictS, dictT)

        for i in dictS:
            if i not in dictT:
                return False

            if dictS[i] != dictT[i]:
                return False
            
        return True

        
# @lc code=end

