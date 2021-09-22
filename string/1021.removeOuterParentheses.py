#对 s 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 s 。

#stack
class Solution:
    def removeOuterParentheses(s: str) -> str:
        stack,res = [],""
        for c in s:
            if c == '(': 
                if stack: res = res + c
                stack.append(c)
            if c == ')':
                stack.pop()
                if stack: res = res + c
        return res
s = "(()())(())"
print(Solution.removeOuterParentheses(s))

#cnt记录外层括号
class Solution1:
    def removeOuterParentheses(s: str) -> str:
        cnt,res = 0,""
        for c in s:
            if c == '(':
                if cnt > 0: res = res + c
            if c == ')':
                if cnt > 1: res = res + c
            cnt += 1 if c == '(' else -1
        return res
s = "(()())(())"
print(Solution1.removeOuterParentheses(s))