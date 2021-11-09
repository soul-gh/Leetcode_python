#给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
        p_A,p_B = headA,headB
        while p_A != p_B:
            if not p_A:
                p_A = headB
            else:
                p_A = p_A.next
            if not p_B:
                p_B = headA
            else:
                p_B = p_B.next
        return p_A
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = ListNode(8)
headB.next.next.next.next = ListNode(4)
headB.next.next.next.next.next = ListNode(5)
p = Solution.getIntersectionNode(headA,headB)
