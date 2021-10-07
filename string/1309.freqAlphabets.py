#给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：
#字符（'a' - 'i'）分别用（'1' - '9'）表示。
#字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
#返回映射之后形成的新字符串。


class Solution:
    def freqAlphabets(s: str) -> str:
        res,i = "",0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                res = res + chr(96 + int(s[i]+s[i+1]))
                i += 3
            else:
                res = res + chr(96 + int(s[i]))
                i += 1
        return res
s = "10#11#12"
print(Solution.freqAlphabets(s)) 