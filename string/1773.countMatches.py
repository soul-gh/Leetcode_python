#给你一个数组 items ，其中 items[i] = [typei, colori, namei] ，描述第 i 件物品的类型、颜色以及名称。
#另给你一条由两个字符串 ruleKey 和 ruleValue 表示的检索规则。
#如果第 i 件物品能满足下述条件之一，则认为该物品与给定的检索规则 匹配 ：
#ruleKey == "type" 且 ruleValue == typei 。
#ruleKey == "color" 且 ruleValue == colori 。
#ruleKey == "name" 且 ruleValue == namei 。
#统计并返回 匹配检索规则的物品数量 。

#普通
class Solution:
    def countMatches(items, ruleKey: str, ruleValue: str) -> int:
        cnt,tmp = 0,0
        if ruleKey == "type":
            tmp = 0
        elif ruleKey == "color":
            tmp = 1
        else:
            tmp = 2
        for i in range(len(items)):
            if items[i][tmp] == ruleValue:
                cnt += 1
        return cnt
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
print(Solution.countMatches(items,ruleKey,ruleValue))