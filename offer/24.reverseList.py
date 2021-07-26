#定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

#三指针迭代
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur :
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

head = ListNode(1)
tmp = head
for i in range(2,6):
    tmp.next = ListNode(i)
    tmp = tmp.next
head = Solution.reverseList(head)
while head:
    print(head.val)
    head = head.next 