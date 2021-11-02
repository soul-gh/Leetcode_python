#给定一个头结点为 head 的非空单链表，返回链表的中间结点。
#如果有两个中间结点，则返回第二个中间结点。

#快慢指针
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(head: ListNode) -> ListNode:
        A,B = head,head
        while B and B.next:
            A = A.next
            B = B.next.next
        return A
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution.middleNode(head).val)