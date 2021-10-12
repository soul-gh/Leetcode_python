#给你一个整数 n，请你返回一个含 n 个字符的字符串，其中每种字符在该字符串中都恰好出现 奇数次 。
#返回的字符串必须只含小写英文字母。如果存在多个满足题目要求的字符串，则返回其中任意一个即可。

#字符串乘法
class Solution:
    def generateTheString(n: int) -> str:
        return 'a' * n if n & 1 else 'a' * (n-1) + 'b'
print(Solution.generateTheString(8))
print(Solution.generateTheString(7))
print(Solution.generateTheString(1))