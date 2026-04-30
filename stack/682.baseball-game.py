#
# @lc app=leetcode id=682 lang=python
#
# [682] Baseball Game
#

# @lc code=start
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        total = 0

        for i in operations:
            if i == '+':
                sum = stack[-1] + stack[-2]
                stack.append(sum)
            elif i == 'D':
                double = stack[-1] * 2
                stack.append(double)
            elif i =='C':
                stack.pop()
            else:
                stack.append(int(i))
            
        for i in stack:
            total += i

        return total 

# @lc code=end

