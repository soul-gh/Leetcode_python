#如果所给格子的颜色是白色，请你返回 true，如果是黑色，请返回 false 。
#给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。

#ord(), asc码换算取余
class Solution:
    def squareIsWhite(coordinates: str) -> bool:
        if (ord(coordinates[0]) + int(coordinates[1])) % 2 == 1:
            return True
        else:
            return False
coordinates = "a1"
print(Solution.squareIsWhite(coordinates))