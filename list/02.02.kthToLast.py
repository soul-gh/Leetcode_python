#实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

#快慢指针
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(head: ListNode, k: int) -> int:
        slow,fast = head,head
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution.kthToLast(head,2))