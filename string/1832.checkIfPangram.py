#全字母句 指包含英语字母表中每个字母至少一次的句子。
#给你一个仅由小写英文字母组成的字符串 sentence ，请你判断 sentence 是否为 全字母句 。
#如果是，返回 true ；否则，返回 false 。

#哈希表
class Solution:
    def checkIfPangram(sentence: str) -> bool:
        dic = {}
        for letter in sentence:
            if letter not in dic:
                dic[letter] = 1
        return len(dic) == 26
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(Solution.checkIfPangram(sentence))

#内置函数
class Solution1:
    def checkIfPangram(sentence: str) -> bool:
        return len(set(sentence)) == 26
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(Solution1.checkIfPangram(sentence))