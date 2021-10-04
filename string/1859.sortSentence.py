#一个 句子 指的是一个序列的单词用单个空格连接起来，且开头和结尾没有任何空格。每个单词都只包含小写或大写英文字母。
#我们可以给一个句子添加 从 1 开始的单词位置索引 ，并且将句子中所有单词 打乱顺序 。
#比方说，句子 "This is a sentence" 可以被打乱顺序得到 "sentence4 a3 is2 This1" 或者 "is2 sentence4 This1 a3" 。
#给你一个 打乱顺序 的句子 s ，它包含的单词不超过 9 个，请你重新构造并得到原本顺序的句子。

#split分割字符串，join合并
class Solution:
    def sortSentence(s: str) -> str:
        s = s.split()
        n = len(s)
        res = [""] * n
        for _ in s:
            res[int(_[-1])-1] = _[:-1]
        return ' '.join(res)
s = "is2 sentence4 This1 a3"
print(Solution.sortSentence(s))