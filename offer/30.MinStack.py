#定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
#辅助栈B。记录最小元素。push时，B空或者x小于B栈顶元素，则也push进B。pop时A与B栈顶元素相同，B也pop
class MinStack:

    def __init__(self):
        self.A = []
        self.B = []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or x <= self.B[-1]:
            self.B.append(x)
    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()
    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.min())
minStack.pop()
print(minStack.top())
print(minStack.min())


