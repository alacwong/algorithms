"""
Node class definition for linked list
"""

from __future__ import annotations


class Node:

    def __init__(self, val=0, _next: Node = None):
        self.val = val
        self.next = _next

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        if self.val != other.val:
            return False

        if self.next:
            return other.next == self.next
        else:
            return other.next is None

    def __str__(self):
        """prettify"""
        if self.next:
            return f'{self.val} -> {self.next}'
        else:
            return f'{self.val}'

    def __lt__(self, other):
        return self.val < other.val

    def __iter__(self):
        return NodeIterator(self)


class NodeIterator:

    def __init__(self, node: Node):
        self.node = node

    def __next__(self):
        if self.node:
            val = self.node.val
            self.node = self.node.next
            return val
        else:
            raise StopIteration


if __name__ == '__main__':
    assert (Node(1) == Node(1)) is True
    assert (Node(1) == Node(3)) is False
    assert (Node(1, Node(2)) == Node(1, Node(2))) is True
    assert str(Node(1, Node(2, Node(3)))) == '1 -> 2 -> 3'
    assert Node(1) < Node(2)
    assert Node(3) > Node(2)
    x = Node(1, Node(5, Node(3, Node(8, Node(10, Node(11, Node(15, Node(18))))))))
