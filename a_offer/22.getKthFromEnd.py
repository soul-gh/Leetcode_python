#一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
#双指针
#快指针先走k个距离，然后两个同步移动到最后，慢的位置则为倒数第k个
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(head: ListNode, k):
        fast, slow = head,head
        for i in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
head = ListNode(1)
tmp = head
for i in range(2,6):
    tmp.next = ListNode(i)
    tmp = tmp.next
head = Solution.getKthFromEnd(head,2)
for i in range(2):
    print(head.val)
    head = head.next 