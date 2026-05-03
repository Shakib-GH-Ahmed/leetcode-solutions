#
# @lc app=leetcode id=901 lang=python
#
# [901]  
#

# @lc code=start
class StockSpanner(object):

    def __init__(self):
        self.price = []       

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        while self.price and price >= self.price[-1][0]:
            span += self.price[-1][1] 
            self.price.pop()

        self.price.append((price,span))
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end