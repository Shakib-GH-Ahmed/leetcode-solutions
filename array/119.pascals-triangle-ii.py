#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        main_List = [1]

        for i in range(rowIndex):
            next_row =  [0] * (len(main_List) + 1)
            
            for j in range(len(main_List)):
                next_row[j] += main_List[j]
                next_row[j + 1] += main_List[j]

            main_List = next_row
              
        
        return main_List
            

            
        
# @lc code=end

