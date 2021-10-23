#复制一个含有random指针的链表

#哈希表
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(head):
        if not head:
            return 
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]
head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = None

head.random = None
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head

res = Solution.copyRandomList(head)
print(res.val)
print(res.next.val)
print(res.random)

#拼接链表，链接，再拆分
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution1:
    def copyRandomList(head):
        if not head:
            return
        cur = head
        while cur:   #拼接
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next

        cur = head
        while cur:   #链接random
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = res = head.next
        pre = head
        while cur.next:   #拆分 pre恢复原链表，cur为复制后的链表
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None   #单独处理原链表末尾
        return res
head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)
head.next.next.next.next.next = None

head.random = None
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head

res = Solution1.copyRandomList(head)
print(res.val)
print(res.next.val)
print(res.random)