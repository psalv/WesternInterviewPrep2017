

class node(object):

    def __init__(self, k=None):
        self.key = k
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return str(self.key)

    def height(self):
        if self.key is None:
            return -1
        else:
            return node.height

    def update_height(self):
        if self.key is None:
            return -1
        else:
            self.height = max(self.height(self.left), self.height(self.right)) + 1


class bst(object):

    def __init__(self):
        self.root = node()

    def find(self, k):
        cur = self.root
        while cur.key is not None:
            if cur.key == k:
                break
            elif cur.key > k:
                cur = cur.left
            else:
                cur = cur.right

        return cur

    def insert(self, k):
        cur = self.root
        while cur.key is not None:
            if cur.key > k:
                cur = cur.left
            else:
                cur = cur.right

        cur.key = k
        cur.left = node()
        cur.right = node()

    def delete(self, k):
        toDelete = self.find(k)
        if toDelete.key is not None:

            # If the node is already a leaf
            if toDelete.right.key is None and toDelete.left.key is None:
                toDelete.key = None
                toDelete.left = None
                toDelete.right = None

            # The case in which the node has no right child
            elif toDelete.right.key is None:
                temp = toDelete.left
                toDelete.key = temp.key
                toDelete.left = temp.left
                toDelete.right = temp.right

            # Otherwise we need to swap with the successor
            else:
                cur = toDelete.right
                while cur.left.key is not None:
                    cur = cur.left
                toDelete.key = cur.key

                # If we are at a leaf node, than delete leaf children
                if cur.right.key is None:
                    cur.key = None
                    cur.left = None
                    cur.right = None

                # Otherwise we remove this node by propagating the ones below it upwards.
                else:
                    temp = cur.right
                    cur.key = temp.key
                    cur.left = temp.left
                    cur.right = temp.right

    def levelOrderTraversal(self):
        q = [self.root]
        while len(q) > 0:
            cur = q.pop(0)

            if cur.left is not None:
                q.append(cur.left)

            if cur.right is not None:
                q.append(cur.right)

            print(cur)


def test():
    tree = bst()
    tree.insert(10)
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(8)
    tree.delete(5)
    tree.levelOrderTraversal()


test()
