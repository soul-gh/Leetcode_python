#给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。
#如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
#返回 合并后的字符串 。

#merge
class Solution:
    def mergeAlternately(word1: str, word2: str) -> str:
        i,j = 0,0
        m,n = len(word1),len(word2)
        res = ""
        while i < m and j < n:
            res = res + word1[i]
            res = res + word2[j]
            i += 1
            j += 1
        while i < m:
            res = res + word1[i]
            i += 1
        while j < n:
            res = res + word2[j]
            j += 1
        return res 
word1 = "abc"
word2 = "pqr"
print(Solution.mergeAlternately(word1,word2))