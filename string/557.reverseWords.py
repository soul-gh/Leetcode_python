#给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

#s[::-1]字符串反转
#[exp for x in y]  对y中每个x进行exp操作(一定要有[],操作后为列表)
class Solution:
    def reverseWords(s: str) -> str:
        return " ".join(word[::-1] for word in s.split())
s = "Let's take LeetCode contest"
print(Solution.reverseWords(s))
