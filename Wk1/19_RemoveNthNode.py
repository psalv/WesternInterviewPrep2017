# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        return

    # This removes the node with value n but we want to remove the nth node
    def removeValFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.val is n:
            return head.next

        if head.next is None:
            return

        if head.next.val is n:
            head.next = head.next.next

        else:
            self.removeNthFromEnd(head.next, n)

        return head

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pos = head
        count = 1
        while pos.next is not None:
            count += 1
            pos = pos.next

        if n > count:
            print("That node does not exist.")
            return

        nodeToDelete = count - n

        if nodeToDelete is 0:
            return head.next


        pos = head
        for i in range(nodeToDelete - 1):
            pos = pos.next

        pos.next = pos.next.next

        return head


    def printLinkedList(self, head):
        if head is not None:
            print(head.val)
            self.printLinkedList(head.next)

    def createMockLinkedList(self):
        # Initializing a test linked list
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(4)
        d = ListNode(8)
        e = ListNode(16)
        f = ListNode(32)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        return a


print("Front of list:")
testA = Solution.createMockLinkedList(Solution())
Solution.printLinkedList(Solution(), Solution.removeNthFromEnd(Solution(), testA, 6))

print("\nMiddle of list A: ")
testB = Solution.createMockLinkedList(Solution())
Solution.printLinkedList(Solution(), Solution.removeNthFromEnd(Solution(), testB, 5))

print("\nMiddle of list B:")
testB = Solution.createMockLinkedList(Solution())
Solution.printLinkedList(Solution(), Solution.removeNthFromEnd(Solution(), testB, 3))

print("\nEnd of list:")
testC = Solution.createMockLinkedList(Solution())
Solution.printLinkedList(Solution(), Solution.removeNthFromEnd(Solution(), testC, 1))

print("\nNot in list:")
testC = Solution.createMockLinkedList(Solution())
Solution.printLinkedList(Solution(), Solution.removeNthFromEnd(Solution(), testC, 9))

