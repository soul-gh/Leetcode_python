#给定一个链表，判断链表中是否有环。
#如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
#为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 
#如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#如果链表中存在环，则返回 true 。 否则，返回 false 。

#快慢指针
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow,fast = head,head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow,fast = slow.next,fast.next.next
        return True
headA = ListNode(3)
headA.next = ListNode(2)
headA.next.next = ListNode(0)
headA.next.next.next = ListNode(-4)
headA.next.next.next.next = headA
print(Solution.hasCycle(headA))

#hash
class Solution1:
    def hasCycle(head: ListNode) -> bool:
        hash_set = []
        cur = head
        while cur:
            if cur in hash_set:
                return True
            hash_set.append(cur)
            cur = cur.next
        return False
headB = ListNode(3)
headB.next = ListNode(2)
headB.next.next = ListNode(0)
headB.next.next.next = ListNode(-4)
headB.next.next.next.next = headB
print(Solution1.hasCycle(headB))