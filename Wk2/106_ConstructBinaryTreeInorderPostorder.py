# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) is 0:
            return None

        memo = {}

        root = TreeNode(postorder[-1])
        for i in range(len(postorder) - 2, -1, -1):
            val = postorder[i]

            current = root
            while True:
                if val not in memo:
                    memo[val] = inorder.index(val)

                if current.val not in memo:
                    memo[current.val] = inorder.index(current.val)

                if memo[val] > memo[current.val]:
                    if current.right is None:
                        current.right = TreeNode(val)
                        break
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = TreeNode(val)
                        break
                    else:
                        current = current.left
        return root

    def recursiveAdd(self, inorder, val, current, memo):
        """
        A recursive solution which is yielded unuseable due to extremely high recursion depths with large trees.
        """
        if val not in memo:
            memo[val] = inorder.index(val)

        if current.val not in memo:
            memo[current.val] = inorder.index(current.val)

        if memo[val] > memo[current.val]:
            if current.right is None:
                current.right = TreeNode(val)
            else:
                self.recursiveAdd(inorder, val, current.right, memo)
        else:
            if current.left is None:
                current.left = TreeNode(val)
            else:
                self.recursiveAdd(inorder, val, current.left, memo)

    def inOrder(self, root, inOrderList):
        if root is not None:
            self.inOrder(root.left, inOrderList)
            inOrderList.append(root.val)
            self.inOrder(root.right, inOrderList)

        return inOrderList

    def postOrder(self, root, postOrderList):
        if root is not None:
            self.postOrder(root.left, postOrderList)
            self.postOrder(root.right, postOrderList)
            postOrderList.append(root.val)

        return postOrderList


def test():
    a = TreeNode(5)
    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(6)
    f = TreeNode(7)
    g = TreeNode(8)

    a.left = c
    a.right = f
    c.left = b
    c.right = d
    f.left = e
    f.right = g

    inOrder = Solution.inOrder(Solution(), a, [])
    postOrder = Solution.postOrder(Solution(), a, [])
    print(inOrder)
    print(postOrder)
    print(Solution.inOrder(Solution(), Solution.buildTree(Solution(), inOrder, postOrder), []))

# test()


