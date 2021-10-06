#给你一个字符串 s ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。

#s.lower()    s.upper()
class Solution:
    def toLowerCase(s: str) -> str:
        return s.lower()
s = "Hello"
print(Solution.toLowerCase(s))

#大写65-90，小写97-122
class Solution1:
    def toLowerCase(s: str) -> str:
        res = ""
        for _ in s:
            if 65 <= ord(_) <= 90 :
                res = res + chr(ord(_) + 32)
            else:
                res = res + _
        return res
s = "Hello"
print(Solution1.toLowerCase(s))