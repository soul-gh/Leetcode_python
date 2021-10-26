#给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。
#请你返回该链表所表示数字的 十进制值 。

#次方：import math  ;   pow(x,y)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(head) -> int:
        import math
        bn,res = [],0
        while head:
            bn.append(head.val)
            head = head.next
        n = len(bn) - 1
        for k in bn:
            res += (k * math.pow(2,n))
            n = n - 1
        return int(res)
head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
print(Solution.getDecimalValue(head))