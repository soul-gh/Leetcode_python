#结果需要取余，其他同14.1。无法使用动态规划。
#直接取最多的3即可
class Solution:
    def cuttingRope(n: int) -> int:
        if n < 4:
            return n-1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return (res*n)%1000000007
        
print(Solution.cuttingRope(5))
