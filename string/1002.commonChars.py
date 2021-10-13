#给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），并以数组形式返回。
#可以按 任意顺序 返回答案。

#以第一个单词的字母为基准，去重。  在后面的字母里统计出现次数最少次数，并将此次数个基准字母加入答案。
#若有单词没有出现基准字母，则为0，不会加入答案。
class Solution:
    def commonChars(words):
        res = ""
        dic = set(words[0])
        for k in dic:
            min_times = min(word.count(k) for word in words)
            res = res + min_times * k
        return list(res)
words = ["bella","label","roller"]
print(Solution.commonChars(words))