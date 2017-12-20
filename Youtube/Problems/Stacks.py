

class threeStacks(object):

    def __init__(self, size=1000):
        self.stacks = []
        self.size = size
        for i in range(self.size):
            self.stacks.append(None)

        self.s1 = 0
        self.s2 = 1
        self.s3 = 2

    def push(self, val, stackNum):
        expand = False

        if stackNum == 1:
            self.stacks[self.s1] = val
            self.s1 += 3

            if self.s1 > self.size:
                expand = True

        elif stackNum == 2:
            self.stacks[self.s2] = val
            self.s2 += 3

            if self.s2 > self.size:
                expand = True

        else:
            self.stacks[self.s3] = val
            self.s3 += 3

            if self.s3 > self.size:
                expand = True

        if expand:
            for i in range(1000):
                self.stacks.append(None)
            self.size += 1000

    def pop(self, stackNum):

        if stackNum == 1:
            self.s1 = max(0, self.s1 - 3)

            toReturn = self.stacks[self.s1]
            self.stacks[self.s1] = None

        elif stackNum == 2:
            self.s2 = max(1, self.s2 - 3)

            toReturn = self.stacks[self.s2]
            self.stacks[self.s2] = None

        else:
            self.s3 = max(2, self.s3 - 3)

            toReturn = self.stacks[self.s3]
            self.stacks[self.s3] = None

        return toReturn
