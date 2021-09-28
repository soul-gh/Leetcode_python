#给你一个字符串 s ，如果 s 是一个 好 字符串，请你返回 true ，否则请返回 false 。
#如果 s 中出现过的 所有 字符的出现次数 相同 ，那么我们称字符串 s 是 好 字符串。

#Counter;  values()提取字典中的值
class Solution:
    def areOccurrencesEqual(s: str) -> bool:
        from collections import Counter
        b = list(Counter(s).values())
        for i in b:
            if i != b[0]:
                return False
        return True
s = "abacbc"
print(Solution.areOccurrencesEqual(s))