class Solution:
    def generate(numRows):
        res = []
        for i in range(1,numRows+1):
            tmp = [1] * i
            for j in range(1,len(tmp)-1):
                tmp[j] = res[i-2][j-1] + res[i-2][j]
            res.append(tmp)
        return res
print(Solution.generate(5))