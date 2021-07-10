#把字符串 s 中的每个空格替换成"%20"
# **Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# **split() 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。       
#遍历添加
class Solution:
    def replaceSpace(s):
        res = []
        for i in range(len(s)):
            if s[i] != ' ':
                res.append(s[i])
            else:
                res.append('%20')
        return "".join(res)

s = "We are happy."
print(Solution.replaceSpace(s))
#split
class Solution1:
    def replaceSpace(s):
        return '%20'.join(s.split(' '))
s = "We are happy."
print(Solution1.replaceSpace(s))