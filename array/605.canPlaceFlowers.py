#种花 不能相邻种
#笨
class Solution:
    def canPlaceFlowers(flowerbed, n):
        if len(flowerbed) <=2:
            if 1 in flowerbed and n != 0 :
                return False
            elif n == 1 or n == 0:
                return True
            else:
                return False
        for i in range(2,len(flowerbed)):
            if i == 2 and flowerbed[i-2] != 1 and flowerbed[i-1] != 1:
                flowerbed[i-2] = 1
                n -= 1
            if i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1
            if flowerbed[i-2] != 1 and flowerbed[i-1] != 1 and flowerbed[i] != 1:
                flowerbed[i-1] = 1
                n -= 1
        if n <= 0:
            return True
        return False
flowerbed = [1,0,0,0,1,0,0]
n = 2
print(Solution.canPlaceFlowers(flowerbed,n))

#前后各加一个0, 可以直接写 [0] + flowerbed + [0]
class Solution1:
    def canPlaceFlowers(flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        cnt = 0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] ==0 and flowerbed[i+1] == 0:
                cnt += 1
                flowerbed[i] = 1
        if cnt >= n:
            return True
        return False
flowerbed = [1,0,0,0,1,0,0]
n = 2
print(Solution1.canPlaceFlowers(flowerbed,n))