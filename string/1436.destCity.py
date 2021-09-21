#给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi]表示该线路将会从 cityAi 直接前往 cityBi 。
#请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。
#题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。

#Counter,切片
class Solution:
    def destCity(paths) -> str:
        from collections import Counter
        tmp = []
        for i in paths:
            for j in i:
                tmp.append(j)
        des = tmp[1::2]
        tmp = Counter(tmp)
        print(tmp)
        for _ in tmp:
            if tmp[_] == 1 and _ in des:
                return _
path = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(Solution.destCity(path))