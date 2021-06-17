class Solution:
    def maxProfit(prices):
        tmp = profit = 0
        for i in range(1,len(prices)):
            tmp = prices[i]-prices[i-1]
            if tmp >0:
                profit += tmp
        return profit
prices = [7,1,5,3,6,4]
print(Solution.maxProfit(prices))