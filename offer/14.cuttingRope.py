#给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
# 请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？

#DP
#至少剪一次，第一次剪的时候剪1没有意义，乘积不会变大，所以从长度2开始剪。
#第二次剪，分为剪和不剪，不剪积为j*（i-j） ，剪则为j*dp[i-j](i-j的长度下的最大积)
class Solution:
    def cuttingRope(n):
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3,n+1):
            for j in range(2,i):
                dp[i] = max(dp[i],max(j*(i-j),j*dp[i-j]))
        return dp[n]
print(Solution.cuttingRope(2))

#尽可能把绳子分成长度为3的小段，这样乘积最大(数学证明)
#1.如果 n == 2，返回1，如果 n == 3，返回2，两个可以合并成n小于4的时候返回n - 1
#2.如果 n == 4，返回4
#3.如果 n > 4，分成尽可能多的长度为3的小段，每次循环长度n减去3，乘积res乘以3；最后返回时乘以小于等于4的最后一小段
#4.上面2和3可以合并

class Solution1:
    def cuttingRope(n):
        if n <= 3:
            return n-1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res*n
print(Solution1.cuttingRope(2))