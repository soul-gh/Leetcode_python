#给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
#在 S 上反复执行重复项删除操作，直到无法继续删除。
#在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

#栈，不断与栈顶元素比较
class Solution:
    def removeDuplicates(s: str) -> str:
        stack = []
        for _ in s:
            if stack and _ == stack[-1]:
                stack.pop()
            else:
                stack.append(_)
        return "".join(stack)
s = "abbaca"
print(Solution.removeDuplicates(s))