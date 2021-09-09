#套一层括号，就代表深度+1，求最大深度

class Solution:
    def maxDepth(s: str) -> int:
        res = 0
        dep = 0
        for _ in s:
            if _ == '(':
                dep += 1
                if dep > res:
                    res = dep
            if _ == ')':
                dep -= 1
        return res
s = "(1+(2*3)+((8)/4))+1"
print(Solution.maxDepth(s))
