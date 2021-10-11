#键盘出现了一些故障，有些字母键无法正常工作。而键盘上所有其他键都能够正常工作。
#给你一个由若干单词组成的字符串 text ，单词间由单个空格组成（不含前导和尾随空格）；
#另有一个字符串 brokenLetters ，由所有已损坏的不同字母键组成，返回你可以使用此键盘完全输入的 text 中单词的数目。

#暴力
class Solution:
    def canBeTypedWords(text: str, brokenLetters: str) -> int:
        words = text.split()
        unuse = 0
        for word in words:
            for letter in word:
                if letter in brokenLetters:
                    unuse += 1
                    break
        return len(words) - unuse
text = "hello world"
brokenLetters = "ad"
print(Solution.canBeTypedWords(text,brokenLetters))

#逐个遍历字符，用标记符flag记录是否存在损坏字符，空格表示一个单词结束，需重置flag
class Solution1:
    def canBeTypedWords(text: str, brokenLetters: str) -> int:
        flag = True
        res = 0
        for ch in text:
            if ch == ' ':
                if flag:
                    res += 1
                else:
                    flag = True
            elif ch in brokenLetters:
                flag = False
        if flag:
            res += 1
        return res 
text = "hello world"
brokenLetters = "ad"
print(Solution1.canBeTypedWords(text,brokenLetters))