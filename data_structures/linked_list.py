# coding: utf-8
"""
链表实际是无序列表的一种实现方式。
"""
class Node(object):
    """Node 是单项链表中的一个基本单位。
    主要有信息域与指针域。
    在单项链表中，一个 node 只知道其下一个元素。
    """
    def __init__(self, info, p=None):
        self._info = info
        self._next = p

    @property
    def info(self):
        return self._info


class LinkedList(object):
    """docstring for LinkedList"""
    def __init__(self):
        self._head = None
        self._length = 0

    def create(self, sequence):
        self._head = Node(sequence[0])
        self._length = len(sequence)
        # 当前起始节点
        p = self._head
        for x in sequence[1:]:
            node = Node(x)
            p._next = node
            p = p._next

    def search(self, search_item):
        p = self._head
        index = 1
        while p is not None:
            if p.info == search_item:
                return index
            else:
                p = p._next
                index += 1
        return -1

    def insert(self, k, value):
        p = self._head
        new_node = Node(value)
        for x in xrange(1, k):
            p = p._next
        after_node = p._next
        p._next = new_node
        new_node = after_node
        self._length += 1

    def remove(self, k):
        p = self._head
        for x in xrange(1, k):
            p = p._next
        remove_node = p._next
        p._next = remove_node._next
        self._length -= 1


class DoubleLinkedNode(Node):
    """docstring for DoubleLinkedNode"""
    def __init__(self):
        super(DoubleLinkedNode, self).__init__()
        self._prev = None


class DoubleLinkedList(object):
    def __init__(self):
        self._head = None
        self._length = 0

    def create(self, sequence):
        self._head = Node(sequence[0])
        self._length = len(sequence)
        # 当前起始节点
        p = self._head
        for x in sequence[1:]:
            node = Node(x)
            p._next = node
            node._prev = p
            p = p._next

    def search(self, search_item):
        p = self._head
        index = 1
        while p is not None:
            if p.info == search_item:
                return index
            else:
                p = p._next
                index += 1
        return -1


if __name__ == '__main__':
    l = LinkedList()
    l.create([1, 2, 3, 4, 5])
    assert l._head.info == 1
    assert l._head._next._next.info == 3
    l.remove(2)
    assert l._head._next._next.info == 4
    assert l._length == 4
    l.insert(2, 8)
    assert l._head._next._next.info == 8
    assert l._length == 5
    assert l.search(1) == 1
