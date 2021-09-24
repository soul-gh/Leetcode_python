#给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。
#两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s 可能同时含有大写和小写字母。
#如果 a 和 b 相似，返回 true ；否则，返回 false 。


#切片，后半边不算最后一个
class Solution:
    def halvesAreAlike(s: str) -> bool:
        n = len(s) // 2
        r = ['a','e','i','o','u','A','E','I','O','U']
        a = s[:n]
        b = s[n:]
        r_a,r_b = 0,0
        for _ in a:
            if _ in r:
                r_a += 1
        for _ in b:
            if _ in r:
                r_b += 1
        return r_a == r_b
s = "book"
print(Solution.halvesAreAlike(s))