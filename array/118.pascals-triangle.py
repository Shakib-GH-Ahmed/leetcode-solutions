#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        main_List = [[1]]

        for i in range(numRows - 1):
            temp  = [0] + main_List[-1] + [0]
            next_row = []
            
            for j in range(len(main_List[-1]) + 1):
                next_row.append(temp[j] + temp[j+1])

            main_List.append(next_row)
        
        return main_List
# @lc code=end

