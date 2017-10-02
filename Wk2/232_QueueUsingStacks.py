
class MyStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.size() is 0


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackEnd = MyStack()
        self.stackFront = MyStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while not self.stackFront.isEmpty():
            self.stackEnd.push(self.stackFront.pop())

        self.stackEnd.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while not self.stackEnd.isEmpty():
            self.stackFront.push(self.stackEnd.pop())

        return self.stackFront.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while not self.stackEnd.isEmpty():
            self.stackFront.push(self.stackEnd.pop())

        return self.stackFront.peek()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stackEnd.isEmpty() and self.stackFront.isEmpty()



