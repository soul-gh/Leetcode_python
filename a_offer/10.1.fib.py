#输出第n项斐波那契数列
#递归超时
class Solution:
    def fib(n: int) -> int:
        if n == 0 :
            return 0
        if n == 1 :
            return 1
        return Solution.fib(n-1) + Solution.fib(n-2)
print(Solution.fib(5))

#非递归
class Solution1:
    def fib(n: int) -> int:
        fib = [0,1]
        if n == 0:
            return fib[0]
        elif n == 1:
            return fib[1]
        else:
            i = 2
            while i <= n:
                fib.append((fib[i-1] + fib[i-2])%(1e9+7))
                i += 1
        return int(fib[n])
print(Solution1.fib(10))

#DP
class Solution2:
    def fib(n: int) -> int:
        a,b = 0,1
        for i in range(n):
            a,b = b,a+b  #************计算方式为先计算右边表达式，然后同时赋值给左边*************
        return a%int(1e9+7)
print(Solution1.fib(10))