#给定一个链表的 头节点 head ，请判断其是否为回文链表。
#如果一个链表是回文，那么链表节点序列从前往后看和从后往前看是相同的。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#放入数组比较倒序（a[::-1]）
class Solution:
    def isPalindrome(head: ListNode) -> bool:
        cur = []
        while head:
            cur.append(head.val)
            head = head.next
        return cur == cur[::-1]
head = ListNode(1)
print(Solution.isPalindrome(head))

