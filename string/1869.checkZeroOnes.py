#给你一个二进制字符串 s 。如果字符串中由 1 组成的 最长 连续子字符串 严格长于 由 0 组成的 最长 连续子字符串，返回 true ；否则，返回false。
#例如，s = "110100010" 中，由 1 组成的最长连续子字符串的长度是 2 ，由 0 组成的最长连续子字符串的长度是 3 。
#注意，如果字符串中不存在 0 ，此时认为由 0 组成的最长连续子字符串的长度是 0 。字符串中不存在 1 的情况也适用此规则。

#双指针
class Solution:
    def checkZeroOnes(s: str) -> bool:
        zero,one,tmp_one,tmp_zero = 0,0,0,0
        for _ in s:
            if _ == '1':
                tmp_one += 1
                if tmp_zero != 0:
                    if tmp_zero > zero:
                        zero = tmp_zero
                    tmp_zero = 0
            else:
                tmp_zero += 1
                if tmp_one != 0:
                    if tmp_one > one:
                        one = tmp_one
                    tmp_one = 0
        if tmp_one > one:
            one = tmp_one
        if tmp_zero > zero:
            zero = tmp_zero
        return one > zero
s = "1101"
print(Solution.checkZeroOnes(s))