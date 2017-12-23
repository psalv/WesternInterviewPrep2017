
class node(object):

    def __init__(self, v):
        self.v = v
        self.next = None

    def __eq__(self, other):
        return self.v == other.v

    def __repr__(self):
        return str(self.v)


def isLinkedListPalindrome(head):
    """
    To do this with extra space is trivial because I would build it into an array.
    Without extra space requires me to know the length of the linked list.

    This is an O(n^2) solution since it amounts to the arithmetic series,
    I bet I can do better than this without extra space.

    """
    n = 0
    cur = head
    while cur is not None:
        n += 1
        cur = cur.next

    cur = head
    for i in range(n // 2):
        toMatch = cur

        for j in range(i, n - i - 1):
            toMatch = toMatch.next

        if toMatch != cur:
            return False

        cur = cur.next

    return True


def recursivePass(curReference, curCopy, n):
    if n == 1:
        if curReference[0] == curCopy:
            curReference[0] = curReference[0].next
            return True
    else:
        if not recursivePass(curReference, curCopy.next, n - 1):
            return False
        else:
            if curReference[0] == curCopy:
                curReference[0] = curReference[0].next
                return True
            else:
                return False


def recursivePalindromic(head):
    n = 0
    cur = head
    while cur is not None:
        n += 1
        cur = cur.next

    cur = head
    toPass = [cur]

    return recursivePass(toPass, cur, n)


def test():

    print("O(n^2) solution, no extra space: ")

    head = node("a")
    head.next = node("b")
    head.next.next = node("a")

    print(isLinkedListPalindrome(head))

    head = node("a")
    head.next = node("b")
    head.next.next = node("b")
    head.next.next.next = node("a")

    print(isLinkedListPalindrome(head))

    head = node("a")
    head.next = node("b")
    head.next.next = node("c")
    head.next.next.next = node("d")
    head.next.next.next.next = node("c")
    head.next.next.next.next.next = node("b")
    head.next.next.next.next.next.next = node("a")

    print(isLinkedListPalindrome(head))

    head = node("a")
    head.next = node("b")
    head.next.next = node("c")

    print(not isLinkedListPalindrome(head))

    print("\nO(n) solution, O(n) extra space needed by recursive stack frames: ")

    head = node("a")
    head.next = node("b")
    head.next.next = node("a")

    print(recursivePalindromic(head))

    head = node("a")
    head.next = node("b")
    head.next.next = node("b")
    head.next.next.next = node("a")

    print(recursivePalindromic(head))

    head = node("a")
    head.next = node("b")
    head.next.next = node("c")
    head.next.next.next = node("d")
    head.next.next.next.next = node("c")
    head.next.next.next.next.next = node("b")
    head.next.next.next.next.next.next = node("a")

    print(recursivePalindromic(head))

    head = node("a")
    head.next = node("b")
    head.next.next = node("c")

    print(not recursivePalindromic(head))


test()
