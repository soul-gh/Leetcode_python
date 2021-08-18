#输入两个链表，找出它们的第一个公共节点。

#哈希表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(headA, headB):
        tmp_a = headA
        tmp_b = headB
        dic = []
        while tmp_a:
            dic.append(tmp_a)
            tmp_a = tmp_a.next
        while tmp_b:
            if tmp_b in dic:
                return tmp_b
            tmp_b = tmp_b.next
        return

#浪漫相遇a+(b-c) = b+(a-c) 
class ListNode:  
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def getIntersectionNode(headA, headB):
        tmp_a = headA
        tmp_b = headB
        while tmp_a != tmp_b:
            tmp_a = tmp_a.next if tmp_a else headB
            tmp_b = tmp_b.next if tmp_b else headA
        return tmp_a