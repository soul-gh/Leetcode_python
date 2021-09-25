#给你一个下标从 0 开始的字符串 word 和一个字符 ch 。找出 ch 第一次出现的下标 i ，
#反转 word 中从下标 0 开始、直到下标 i 结束（含下标 i ）的那段字符。如果 word 中不存在字符 ch ，则无需进行任何操作。
#例如，如果 word = "abcdefd" 且 ch = "d" ，那么你应该 反转 从下标 0 开始、直到下标 3 结束（含下标 3 ）。结果字符串将会是 "dcbaefd" 。
#返回 结果字符串 。

#
class Solution:
    def reversePrefix(word: str, ch: str) -> str:
        if ch not in word:
            return word
        left,res = 0,""
        for i in range(len(word)):
            if word[i] == ch:
                left = i
                break
        for j in range(left,-1,-1):
            res = res + word[j]
        return res + word[left+1::]
word = "abcdefd"
ch = "d"
print(Solution.reversePrefix(word,ch))