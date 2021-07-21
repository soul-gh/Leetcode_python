#实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。
#超时
class Solution:
    def myPow(x: float, n: int) -> float:
        if n == 0:
            return float(1)
        if n > 0:
            res = x
            for i in range(1,n):
                res *= x
            return res
        if n < 0:
            res = x
            for i in range(1,-n):
                res *= x
            return 1/res
print(Solution.myPow(2.0,0))

#递归
# n & 1 等于1 则n为奇数
# 幂数分为奇和偶，奇数化为x*偶数次幂。 偶数则化为x^2*(n/2).（为了实现每次递归二分）
class Solution:
    def myPow(x: float, n: int) -> float:
        if n == 0:
            return float(1)
        elif n < 0:
            return 1 / Solution.myPow(x,-n)
        elif n & 1:
            return x * Solution.myPow(x,n-1)
        else:
            return Solution.myPow(x*x,n//2) 
print(Solution.myPow(2.0,10))

#快速幂
class Solution:
    def myPow(x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            n = -n
            x = 1/x
        res = 1.0
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res 
