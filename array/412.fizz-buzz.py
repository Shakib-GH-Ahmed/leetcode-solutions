#
# @lc app=leetcode id=412 lang=python
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []

        for i in range(1, n+1):
            if i % 3 == 0:
                char = "Fizz"
                if i % 5 == 0:
                    char += "Buzz"
            elif i % 5 == 0:
                char = "Buzz"
            else:
                char = str(i)
                
            answer.append(char)
        
        return answer
    
# @lc code=end