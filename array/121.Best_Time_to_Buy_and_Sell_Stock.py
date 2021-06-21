#一次遍历，双指针，start记录当前最小买进价格，profit记录当前最大收益
class Solution:
    def maxProfit(prices):
        profit = start = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[start]:
                start = i
            profit = max(prices[i]-prices[start],profit)
        return profit
prices = [1,7,5,3,6,4]
print(Solution.maxProfit(prices))

#超时
class Solution1:
    def maxProfit(prices):
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]:
                buy = i
            elif prices[i]>prices[i-1]:
                buy = i-1
                for j in range(buy+1,len(prices)):
                    if prices[j] - prices[buy] > profit:
                        profit = prices[j] - prices[buy]
        return profit
prices = [1,7,5,3,6,4]
print(Solution1.maxProfit(prices))



