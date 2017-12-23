
def findSuccessor(node):

    # If it has a right child
    if node.right is not None:
        cur = node.right
        while cur.left is not None:
            cur = cur.left
        return cur

    # Else go up to parents
    else:
        cur = cur.parent
        while cur is not None:
            if cur.key >= node.key:
                return cur
            cur = cur.parent
        return None


