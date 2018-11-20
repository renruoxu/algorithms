class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            self.stack = self.stack[:-1]
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return min(self.stack)
        
import collections
class MinStack2(object):
    def __init__(self):
        """Implementation using deque"""
        self.deque = collections.deque()

    def push(self, x):
        self.deque.append(x)

    def pop(self):
        if len(self.deque) > 0:
            self.deque.pop()

    def top(self):
        if len(self.deque) > 0:
            a = self.deque.pop()
            self.deque.append(a)
            return a

    def getMin(self):
        if len(self.deque) > 0:
            return min(self.deque)
