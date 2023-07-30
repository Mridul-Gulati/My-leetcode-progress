class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_point = 0
        sell_point = 1
        profit = 0
        
        while buy_point < len(prices) and sell_point < len(prices):
            if prices[buy_point] > prices[sell_point]:
                buy_point = sell_point
                sell_point+=1
            else:
                profit = max(profit,prices[sell_point] - prices[buy_point])
                sell_point+=1
        return profit
                