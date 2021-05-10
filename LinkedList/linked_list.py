"""
Algorithm practice with linked lists
"""

from LinkedList.node import Node
from solver import Solver
import heapq


class RemoveDuplicates(Solver):

    def solve(self, head: Node):

        if not head:
            return None

        s = set()
        curr = head
        while curr.next:
            s.add(curr.val)

            # remove duplicate
            if curr.next.val in s:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

    def __init__(self):
        super().__init__()
        self.test_cases = [
            ({'head': None}, None),
            ({'head': Node(1)}, Node(1)),
            ({'head': Node(1, _next=Node(2))}, Node(1, _next=Node(2))),
            ({'head': Node(1, _next=Node(1, _next=Node(1, _next=Node(2))))}, Node(1, _next=Node(2)))
        ]


class KtoN(Solver):

    def solve(self, head: Node, k: int):
        """
        Return to kth last element from a singly linked list
        """
        heap = [-val for val in head]
        heapq.heapify(heap)
        ans = 0
        for i in range(k + 1):
            ans = -1 * heapq.heappop(heap)
        return ans

    def __init__(self):
        super().__init__()
        self.test_cases = [
            ({'head': Node(1, Node(5, Node(3, Node(8, Node(10, Node(11, Node(15, Node(18)))))))), 'k': 1}, 15)
        ]


if __name__ == '__main__':
    RemoveDuplicates().run_cases()
    KtoN().run_cases()
