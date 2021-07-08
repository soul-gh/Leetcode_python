#两个列表的最小索引总和（相同元素）
#哈希表
class Solution:
    def findRestaurant(list1, list2):
        res = []
        hash_map = {}
        min_index = float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    hash_map[list1[i]] = i+j
        min_index = min(hash_map.values())
        for k,v in hash_map.items():
            if v == min_index:
                res.append(k)                   
        return res
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
print(Solution.findRestaurant(list1,list2))