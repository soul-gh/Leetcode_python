#输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

#pow,幂.   同**
class Solution:
    def printNumbers(n: int):
        res = []
        for i in range(1,10 ** n):
            res.append(i)
        return res 
print(Solution.printNumbers(3))

#位数全排列
class Solution:
    def printNumbers(n: int):
        def dfs(index,num,digit):
            if index == digit:
                res.append(int(''.join(num)))
                return
            for i in range(10):
                num.append(str(i))
                dfs(index+1,num,digit)
                num.pop()
        res = []
        for digit in range(1,n+1):
            for first in range(1,10):
                num = [str(first)]
                dfs(1,num,digit)
        return res 
print(Solution.printNumbers(3))