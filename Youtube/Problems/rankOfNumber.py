

class binarynode(object):
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.rank = 0

    def __repr__(self):
        return "\nNode: " + str(self.val) + "\nRank: " + str(self.rank)


class binarytree(object):

    def __init__(self):
        self.root = binarynode()

    def addNode(self, val):

        if self.root.val is None:
            self.root.val = val
            self.root.left = binarynode()
            self.root.right = binarynode()

        else:
            cur = self.root
            while cur.val is not None:

                if cur.val < val:
                    temp = cur.rank

                    cur = cur.right
                    cur.rank = temp + 1

                else:
                    cur.rank += 1
                    cur = cur.left

            cur.val = val
            cur.left = binarynode()
            cur.right = binarynode()

    def inorderTraversal(self, node):

        if node.val is None:
            return

        self.inorderTraversal(node.left)
        print(node)
        self.inorderTraversal(node.right)

    def printTree(self):
        self.inorderTraversal(self.root)


def test():
    tree = binarytree()
    tree.addNode(3)
    tree.addNode(2)
    tree.addNode(1)
    tree.addNode(4)
    tree.addNode(5)
    tree.addNode(-1)
    tree.addNode(100)

    tree.printTree()


test()
