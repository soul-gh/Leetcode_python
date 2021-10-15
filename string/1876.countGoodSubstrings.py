#如果一个字符串不含有任何重复字符，我们称这个字符串为 好 字符串。
#给你一个字符串 s ，请你返回 s 中长度为 3 的 好子字符串 的数量。
#注意，如果相同的好子字符串出现多次，每一次都应该被记入答案之中。
#子字符串 是一个字符串中连续的字符序列。

#切片末尾参数不包含末尾
class Solution:
    def countGoodSubstrings(s: str) -> int:
        res = 0
        for i in range(2,len(s)):
            if len(set(s[i-2:i+1])) == 3:
                res += 1
        return res
s = "xyzzaz"
print(Solution.countGoodSubstrings(s))