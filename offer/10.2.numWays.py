#青蛙跳台阶问题.一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
#同斐波那契数列
#DP
class Solution:
    def numWays(n: int) -> int:
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2
        d = [0]*(n+1)
        d[0],d[1],d[2]= 1,1,2
        for i in range(3,n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]%1000000007
print(Solution.numWays(7))

#DP
class Solution1:
    def numWays(n: int) -> int:
        cur, nxt = 1, 1
        for _ in range(n):
            cur, nxt = nxt, cur + nxt
        return cur % 1000000007
print(Solution.numWays(7))
