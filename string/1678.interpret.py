#请你设计一个可以解释字符串 command 的 Goal 解析器 。
#command 由 "G"、"()" 和/或 "(al)" 按某种顺序组成。
#Goal 解析器会将 "G" 解释为字符串 "G"、"()" 解释为字符串 "o" ，"(al)" 解释为字符串 "al" 。
#然后，按原顺序将经解释得到的字符串连接成一个字符串。

#replace替换
class Solution:
    def interpret(command: str) -> str:
        command = command.replace("()","o")
        command = command.replace("(al)","al")
        return command
command = "G()(al)"
print(Solution.interpret(command))

#循环遍历，替换
class Solution1:
    def interpret(command: str) -> str:
        res,i = '',0
        while i < len(command):
            if command[i:i+2] == '()':
                res = res + 'o'
                i += 2
            elif command[i:i+4] == "(al)":
                res = res + "al"
                i += 4
            else:
                res = res + command[i]
                i += 1
        return res 
command = "G()(al)"
print(Solution1.interpret(command))