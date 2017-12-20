
class node(object):
    def __init__(self, v):
        self.next = None
        self.v = v

    def __repr__(self):
        return str(self.v)


def printLinkedList(head):
    while head is not None:
        print(head)
        head = head.next


# Delete duplicates from a linked list
def deleteDuplicates(head):
    seen = set()
    seen.add(head.v)

    cur = head.next
    prev = head

    while cur is not None:
        if not (cur.v in seen):
            seen.add(cur.v)
            prev = cur
        else:
            prev.next = cur.next

        cur = cur.next


def findKthLast(head, k):
    n = 0
    cur = head
    while cur is not None:
        n += 1
        cur = cur.next

    for i in range(n - k):
        head = head.next

    return head


def deleteNodeGivenNode(n):
    while n is not None:
        nextNode = n.next

        if nextNode is not None:
            n.v = nextNode.v

        if nextNode.next is None:
            n.next = None

        n = n.next


def circularList(head):
    seen = set()
    while head is not None:
        if head not in seen:
            seen.add(head)
            head = head.next
        else:
            return head

    return -1


def tests():

    def generateLinkedList():
        a = node('a')
        b = node('b')
        c = node('c')
        d = node('d')
        e = node('e')
        f = node('d')

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        return a

    print("Remove Duplicates:")

    head = generateLinkedList()
    deleteDuplicates(head)
    printLinkedList(head)

    print("\nKth Last:")
    print(findKthLast(generateLinkedList(), 4))

    print("\nDelete middle:")
    head = generateLinkedList()
    deleteNodeGivenNode(head.next.next)
    printLinkedList(head)

    print("\nCircular list:")
    head = generateLinkedList()
    head.next.next.next = head.next
    print(circularList(head))


tests()

