#输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

#归并
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        res = []
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                res.append(l1.val)
                l1 = l1.next
            else:
                res.append(l2.val)
                l2 = l2.next
        if l1:
            while l1:
                res.append(l1.val)
                l1 = l1.next
        if l2:
            while l2:
                res.append(l2.val)
                l2 = l2.next
        if len(res) == 0:
            return None
        head = ListNode(res[-1])
        for i in range(len(res)-2,-1,-1):
            node = ListNode(res[i])
            node.next = head
            head = node 
        return head
l1 = [1,2,4]
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

l2 = [1,3,4]
head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
head = Solution.mergeTwoLists(head1,head2)
while head:
    print(head.val)
    head = head.next 

#伪头节点
class Solution1:
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        dum = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else :
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next
head = Solution1.mergeTwoLists(head1,head2)
while head:
    print(head.val)
    head = head.next 