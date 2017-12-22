
class node(object):
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.v)


def inOrderTraversal(root):
    if root is None:
        return

    inOrderTraversal(root.left)
    print(root)
    inOrderTraversal(root.right)


def preOrderTraversal(root):
    if root is None:
        return

    print(root)
    inOrderTraversal(root.left)
    inOrderTraversal(root.right)


def levelOrderTraversal(root):
    q = [root]
    while len(q) > 0:
        cur = q.pop(0)

        if cur.left is not None:
            q.append(cur.left)

        if cur.right is not None:
            q.append(cur.right)

        print(cur)


def createBstFromSorted(ar):
    length = len(ar)
    if length == 1:
        return node(ar[0])

    else:
        middle = length // 2
        root = node(ar[middle])

        root.left = createBstFromSorted(ar[:middle])
        root.right = createBstFromSorted(ar[middle + 1:])

        return root


def test():
    ar = [1, 2, 3, 4, 5, 6, 7]
    root = createBstFromSorted(ar)

    print("In order:")
    inOrderTraversal(root)

    print("\nPre order:")
    preOrderTraversal(root)

    print("\nLevel order:")
    levelOrderTraversal(root)


test()
