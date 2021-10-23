#输入是一个无符号整数(十进制)，返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。

class Solution:
    def hammingWeight(n: int) -> int:
        cnt = 0
        while n != 0:
            if n % 2 == 1:
                cnt += 1
            n //= 2
        return cnt
print(Solution.hammingWeight(11))