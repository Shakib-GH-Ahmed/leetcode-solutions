#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a StringFind All Anagrams in a String
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        
        s_count = {}
        p_count = {}
        l = 0

        for i in range(len(p)):
            if p[i] in p_count:
                p_count[p[i]] += 1
            else:
                p_count[p[i]] = 1 
            
            if s[i] in s_count:
                s_count[s[i]] += 1
            else:
                s_count[s[i]] = 1
     
        if s_count == p_count:
            answer = [0]
        else:
           answer = []

        for r in range(len(p), len(s)):
            if s[r] in s_count:
                s_count[s[r]] += 1
            else:
                s_count[s[r]] = 1

            s_count[s[l]] -= 1
            if s_count[s[l]] == 0:
                s_count.pop(s[l])

            l += 1
            if s_count == p_count:
                answer.append(l) 
            
        return answer



# @lc code=end