#给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。

#添加头节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(head: ListNode) -> ListNode:
        pre,cur = None,head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre,cur = cur,tmp
        return pre
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head = Solution.reverseList(head)
while head:
    print(head.val)
    head = head.next