#不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
#实现 MyHashSet 类：
#void add(key) 向哈希集合中插入值 key 。
#bool contains(key) 返回哈希集合中是否存在这个值 key 。
#void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

#做一个与要求等长的表
class MyHashSet:

    def __init__(self):
        self.hash_ = [False] * 1000001

    def add(self, key: int) -> None:
        self.hash_[key] = True

    def remove(self, key: int) -> None:
        self.hash_[key] = False

    def contains(self, key: int) -> bool:
        return self.hash_[key]