#给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。
#如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。
#请你返回 words 数组中 一致字符串 的数目。

#暴力
class Solution:
    def countConsistentStrings(allowed: str, words) -> int:
        cnt = 0
        for word in words:
            for i in range(len(word)):
                if word[i] in allowed:
                    if i == len(word) - 1:
                        cnt += 1
                    continue
                else:
                    break
        return cnt
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(Solution.countConsistentStrings(allowed,words))
