#请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(node):
        node.val = node.next.val
        node.next = node.next.next
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
Solution.deleteNode(head.next)
for i in range(3):
    print(head.val)
    head = head.next 