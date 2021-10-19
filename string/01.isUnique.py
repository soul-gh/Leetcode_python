#实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

#set去重
class Solution:
    def isUnique(astr: str) -> bool:
        return len(set(astr)) == len(astr)
s = "leetcode"
print(Solution.isUnique(s))