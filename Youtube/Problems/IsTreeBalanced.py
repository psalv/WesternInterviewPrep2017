
class node(object):

    def __init__(self, k=None):
        self.key = k
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.key)


def recursiveFind(root):
    if root is None:
        return -1
    else:
        left = recursiveFind(root.left)
        right = recursiveFind(root.right)

        if left is False or right is False:
            return False

        if abs(left - right) > 1:
            return False
        else:
            return max(left, right) + 1


def isTreeBalanced(root):
    return False is not recursiveFind(root)


def isBinarySearchTree(root):
    if root is None:
        return True

    if not isBinarySearchTree(root.left):
        return False

    if root.left is not None and root.left.key > root.key:
        return False

    if root.right is not None and root.right.key < root.key:
        return False

    if not isBinarySearchTree(root.right):
        return False

    return True


def test():
    root = node(10)
    root.left = node(5)
    root.right = node(15)

    root.left.left = node(3)
    root.left.right = node(6)

    root.right.left = node(12)
    root.right.right = node(17)

    print(isTreeBalanced(root))

    root = node(10)
    root.left = node(5)
    root.right = node(15)

    root.left.left = node(3)

    root.right.left = node(12)
    root.right.right = node(17)

    print(isTreeBalanced(root))

    root = node(10)
    root.left = node(5)
    root.right = node(15)

    root.left.left = node(3)
    root.left.left.left = node(1)

    root.right.left = node(12)
    root.right.right = node(17)

    print(not isTreeBalanced(root))


def testBST():
    root = node(10)
    root.left = node(5)
    root.right = node(15)

    root.left.left = node(3)
    root.left.right = node(6)

    root.right.left = node(12)
    root.right.right = node(17)

    print(str(isBinarySearchTree(root)))

    root = node(10)
    root.left = node(5)
    root.right = node(15)

    root.left.left = node(3)

    root.right.left = node(12)
    root.right.right = node(17)

    print(str(isBinarySearchTree(root)))

    root = node(10)
    root.left = node(5)
    root.right = node(15)

    root.left.left = node(3)
    root.left.left.left = node(1)

    root.right.left = node(12)
    root.right.right = node(17)

    print(str(isBinarySearchTree(root)))

    root = node(10)
    root.left = node(5)
    root.right = node(7)

    print(str(not isBinarySearchTree(root)))

    root = node(10)
    root.left = node(5)
    root.left.left = node(7)

    print(str(not isBinarySearchTree(root)))

    root = node(10)

    print(str(isBinarySearchTree(root)))


print("Balanced:")
test()
print("\nRI:")
testBST()
