from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractStack(ABC):

    @abstractmethod
    def push(self, val: int):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def pop(self):
        pass


class StackNode:

    def __init__(self, val: int, stack: StackNode = None):
        self.val = val
        self.stack = stack


class Stack(AbstractStack):
    """
    basic stack class
    """

    def push(self, val: int):
        self.top = StackNode(val=val, stack=self.top)
        self.count += 1

    def peek(self):
        return self.top.val

    def pop(self):
        top = self.top
        self.top = self.top.stack
        return top.val

    def __len__(self):
        return self.count

    def __init__(self, top: StackNode = None):
        self.top = top
        self.count = 0
