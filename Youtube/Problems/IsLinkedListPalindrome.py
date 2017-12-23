
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


def test():
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


test()
