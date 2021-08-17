#在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

#哈希表
class Solution:
    def firstUniqChar(s: str) -> str:
        dic = {}
        for _ in s:
            if _ not in dic:
                dic[_] = True
            else:
                dic[_] = False
        for k,v in dic.items():
            if v:
                return k
        return " "
        
s = "leetcode"
print(Solution.firstUniqChar(s))