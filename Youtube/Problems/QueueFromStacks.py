
class queueFromStack(object):

    def __init__(self):

        self.stack = []
        self.stack_buffer = []

    def enqueue(self, v):
        """O(1) operation"""
        self.stack.append(v)

    def dequeue(self):
        """O(n) operation, since it requires us to move each element to get at the first one"""
        if len(self.stack) == 0:
            return None

        while len(self.stack) != 1:
            self.stack_buffer.append(self.stack.pop())

        toReturn = self.stack.pop()

        while len(self.stack_buffer) != 0:
            self.stack.append(self.stack_buffer.pop())

        return toReturn


def test():
    q = queueFromStack()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print(1 == q.dequeue())
    print(2 == q.dequeue())
    print(3 == q.dequeue())
    print(4 == q.dequeue())

    q.enqueue(6)

    print(5 == q.dequeue())
    print(6 == q.dequeue())
    print(None is q.dequeue())


test()


