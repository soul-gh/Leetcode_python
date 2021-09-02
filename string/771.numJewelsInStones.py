# 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。
# S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

#普通
class Solution:
    def numJewelsInStones(jewels: str, stones: str) -> int:
        res = 0
        for _ in stones:
            if _ in jewels:
                res += 1
        return res 
jewels = "aA"
stones = "aAAbbbb"
print(Solution.numJewelsInStones(jewels,stones))

#哈希表
class Solution1:
    def numJewelsInStones(jewels: str, stones: str) -> int:
        dic = {}
        res = 0
        for _ in jewels:
            dic[_] = 0
        for _ in stones:
            if _ in dic:
                dic[_] += 1
        for i in dic:
            res += dic[i]
        return res
jewels = "aA"
stones = "aAAbbbb"
print(Solution1.numJewelsInStones(jewels,stones))
