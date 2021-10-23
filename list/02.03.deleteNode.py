#若链表中的某个节点，既不是链表头节点，也不是链表尾节点，则称其为该链表的「中间节点」。
#假定已知链表的某一个中间节点，请实现一种算法，将该节点从链表中删除。
#例如，传入节点 c（位于单向链表 a->b->c->d->e->f 中），将其删除后，剩余链表为 a->b->d->e->f

#只改变数据位置
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