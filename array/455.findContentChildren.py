#小孩吃饼干
#双指针
class Solution:
    def findContentChildren(g, s):
        cnt = 0
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cnt += 1
                i += 1
                j += 1
            else:
                j += 1
        return cnt
g = [1,2,3]
s = [1,1]
print(Solution.findContentChildren(g,s))