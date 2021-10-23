#链表反转
#**切片[::-1]
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    def reversePrint(head):
        tmp = []
        res = []
        while head != None:
            tmp.append(head.val)
            head = head.next
        return tmp[::-1]
node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(2)
node1.next = node2
node2.next = node3
print(Solution.reversePrint(node1))