#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
        
        if s1_counts == s2_counts:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            s2_counts[ord(s2[r]) - ord('a')] += 1
            s2_counts[ord(s2[l]) - ord('a')] -= 1

            if s1_counts == s2_counts:
                return True
            l += 1
        
        return False
            
    
# @lc code=end