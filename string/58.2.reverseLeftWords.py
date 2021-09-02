#字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

#切片
class Solution:
    def reverseLeftWords(s: str, n: int) -> str:
        return s[n:] + s[:n]
print(Solution.reverseLeftWords("abcdefg",2))

#字符串遍历拼接
class Solution1:
    def reverseLeftWords(s: str, n: int) -> str:
        res = ""
        for i in range(n,len(s) + n):
            res += s[i % len(s)]
        return res
print(Solution1.reverseLeftWords("abcdefg",2))