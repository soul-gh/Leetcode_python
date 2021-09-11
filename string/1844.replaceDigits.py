#给你一个下标从 0 开始的字符串 s ，它的 偶数 下标处为小写英文字母，奇数 下标处为数字。
#定义一个函数 shift(c, x) ，其中 c 是一个字符且 x 是一个数字，函数返回字母表中 c 后面第 x 个字符。
#shift('a', 5) = 'f' 和 shift('x', 0) = 'x' 。

#isdigit:判断是否为数字。     'A'.ord():A所对应的asc码
class Solution:
    def replaceDigits(s: str) -> str:
        res = ''
        for i in range(len(s)):
            if s[i].isdigit():
                res = res + chr(ord(s[i-1]) + int(s[i]))
            else:
                res = res + s[i]
        return res
s = "a1c1e1"
print(Solution.replaceDigits(s))