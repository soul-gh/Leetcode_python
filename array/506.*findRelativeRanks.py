#排名
#enumerte枚举函数，可访问两个数据：键和值
#get函数，获取字典中指定键所对应的值
class Solution:
    def findRelativeRanks(score):
        res = []
        hash_map = {}
        tmp = sorted(score,reverse = True)
        start = 1
        for k,v in enumerate(tmp):
            if start == 1:
                hash_map[v] = 'Gold Medal'
            if start == 2:
                hash_map[v] = 'Silver Medal'
            if start == 3:
                hash_map[v] = 'Bronze Medal'
            if start > 3:
                hash_map[v] = str(start)
            start += 1
        for i in range(len(score)):
            res.append(hash_map.get(score[i]))
        return res
score = [5,4,3,2,1]
print(Solution.findRelativeRanks(score))
