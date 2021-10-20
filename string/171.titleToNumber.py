#给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。

#A:65
class Solution:
    def titleToNumber(columnTitle: str) -> int:
        res = 0
        for a in columnTitle:
            res *= 26
            res += (ord(a) - 64)
        return res
print(Solution.titleToNumber(columnTitle="AB"))