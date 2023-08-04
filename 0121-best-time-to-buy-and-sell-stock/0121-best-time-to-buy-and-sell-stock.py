class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        n = len(prices)
        max_profit = 0
        while i<n and j<n:
            profit = prices[j] - prices[i]
            if profit<=0:
                i = j
                j +=1
            else:
                max_profit = max(profit,max_profit)
                j+=1
        return max_profit
                