#给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
#所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。

#写一个新字符串
class Solution:
    def defangIPaddr(address: str) -> str:
        res = ""
        for _ in address:
            if _ != ".":
                res = res + _
            else:
                res = res + "[.]"
        return res
address = "1.1.1.1"
print(Solution.defangIPaddr(address))

#python特性,replace字符串替换
class Solution1:
    def defangIPaddr(address: str) -> str:
        return address.replace(".","[.]")
address = "1.1.1.1"
print(Solution1.defangIPaddr(address))