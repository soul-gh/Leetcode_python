#给你两个字符串数组 word1 和 word2 。如果两个数组表示的字符串相同，返回 true ；否则，返回 false 。

#''.join(数组)
class Solution:
    def arrayStringsAreEqual(word1, word2) -> bool:
        return ''.join(word1) == ''.join(word2)
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(Solution.arrayStringsAreEqual(word1,word2))