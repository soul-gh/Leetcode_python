#在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。
#给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
#注意：分割得到的每个字符串都必须是平衡字符串。
#返回可以通过分割得到的平衡字符串的 最大数量 。

#贪心算法，每一步都记下LR的个数，个数相等则分割一次
class Solution:
    def balancedStringSplit(s: str) -> int:
        left,right,res = 0,0,0
        for i in s:
            if i == 'L':
                left += 1
            elif i == 'R':
                right += 1
            if left == right:
                res += 1
        return res
s = "RLRRLLRLRL"
print(Solution.balancedStringSplit(s))