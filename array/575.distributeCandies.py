#分糖果
#超时
class Solution:
    def distributeCandies(candyType):
        n = len(candyType)
        sis = []
        for i in range(n):
            if candyType[i] not in sis and len(sis) < n//2:
                sis.append(candyType[i])
        return len(sis)
nums = [1,1,2,2,3,3]
print(Solution.distributeCandies(nums))

#思路一样，不实用in函数
class Solution1:
    def distributeCandies(candyType):
        candyType.sort()
        sis = [candyType[0]]
        for i in range(1,len(candyType)):
            if candyType[i] != candyType[i-1] and len(sis) < len(candyType)//2:
                sis.append(candyType[i])
        return len(sis)
nums = [1,1,2,2,3,3]
print(Solution1.distributeCandies(nums))

#set去重
class Solution2:
    def distributeCandies(candyType):
        return min(len(set(candyType)),len(candyType)//2)
nums = [1,1,2,2,3,3]
print(Solution2.distributeCandies(nums))