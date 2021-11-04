#编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

#hash
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(head: ListNode) -> ListNode:
        if not head:
            return head
        p,dic = head,[head.val]
        while p.next:
            if p.next.val not in dic:
                dic.append(p.next.val)
                p = p.next
            else:
                p.next = p.next.next
        return head
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(2)
Solution.removeDuplicateNodes(head)
while head:
    print(head.val)
    head = head.next