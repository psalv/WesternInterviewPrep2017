
import math


class HashTableOpenAddressing(object):
    """
    Open addressing hash table.
    Will need to use double hashing to find a new spot.

    h(k, i) = ( h1(k) + i * h2(k) ) % m
    m = size of hash table
    h1 and h2 are hash functions

    We continually increase i until we find an open spot
    When we delete we set a flag to continue searching
    """

    def __init__(self, m=None):
        """
        If the hash table is not initialized with a size it will default to 1000 elements
        """
        self.p = 452930477

        self.a1 = math.floor(self.p / 4)
        self.a2 = math.floor(self.p / 3)
        self.b1 = math.floor(self.p / 8)
        self.b2 = math.floor(self.p / 6)

        self.m = m
        if self.m is None:
            self.m = 1000

        self.table = [None] * m
        self.num = 0

    def _h1(self, k):
        """
        A universal hash function of the form h1(k) = (ak + b) % p
        """
        return (self.a1 * hash(k) + self.b1) % self.p

    def _h2(self, k):
        """
        A universal hash function of the form h2(k) = (ak + b) % p
        """
        return (self.a2 * hash(k) + self.b2) % self.p

    def _h(self, k, i):
        """
        Double hashing to facilitate open addressing
        """
        return int((self._h1(k) + i * self._h2(k)) % self.m)

    def insert(self, k):
        """
        Inserts into the table, when the table is 40% full we double it's size (to avoid lengthy hashing loops)
        Time should be amortized to O(1)
        """
        if self.m < self.num * 2.5:
            self.m *= 2
            newTable = [None] * self.m

            for k in self.table:
                i = 0
                curIndex = self._h(k, i)
                while newTable[curIndex] is not None:
                    i += 1
                    curIndex = self._h(k, i)

                newTable[curIndex] = k

            self.table = newTable

        i = 0
        curIndex = self._h(k, i)
        while self.table[curIndex] is not None and self.table[curIndex] != "__OPEN__":
            if self.table[curIndex] is k:
                return False

            i += 1
            curIndex = self._h(k, i)

        self.table[curIndex] = k
        self.num += 1
        return True

    def contains(self, k):
        """
        Check to see if an element is contained within the hash table
        """
        i = 0
        curIndex = self._h(k, i)
        while self.table[curIndex] is not None:
            if self.table[curIndex] == k:
                return True

            i += 1
            curIndex = self._h(k, i)

        return False

    def delete(self, k):
        """
        Deletes an element from the hash table and replaces it with __OPEN__,
        such that future searches will bipass this spot to keep looking
        """
        i = 0
        curIndex = self._h(k, i)
        while self.table[curIndex] is not None:
            if self.table[curIndex] == k:

                self.table[curIndex] = "__OPEN__"
                self.num -= 1
                return k

            i += 1
            curIndex = self._h(k, i)

        return False

    def size(self):
        """
        The number of elements in the hash table
        """
        return self.num


def testOpenHashTable():
    openTable = HashTableOpenAddressing(1000)
    openTable.insert("hello")
    openTable.insert("world")
    openTable.insert("this")
    openTable.insert("is")
    openTable.insert("paul")
    openTable.insert("paul")

    print(openTable.contains("paul"))
    print(openTable.contains("paulo"))

    openTable.delete("paul")
    print(openTable.contains("paul"))

    openTable.delete("paul")
    print(openTable.contains("paul"))


print("\nTesting Open Addressed Table\n")
testOpenHashTable()


class HashTableChaining(object):
    """
    Chaining hash table.
    Should have a load of nums/m, making look up O(nums/m)
    """

    def __init__(self, m=None):
        """
        If the hash table is not initialized with a size it will default to 1000 elements
        """
        self.p = 452930477

        self.a = math.floor(self.p / 4)
        self.b = math.floor(self.p / 8)

        self.m = m
        if self.m is None:
            self.m = 1000

        self.table = [None] * m
        self.num = 0

    def h(self, k):
        """
        Universal hash
        """
        return (int(self.a * hash(k) + self.b) % self.p) % self.m

    def insert(self, k):
        """
        Insert into an array, creates array if one does not yet exist
        """
        key = self.h(k)
        if self.table[key] is None:
            self.table[key] = [k]
        else:
            for item in self.table[key]:
                if item == k:
                    return False

            self.table[key].append(k)

        self.num += 1
        return True

    def contains(self, k):
        """
        Checks if an element exists
        """
        key = self.h(k)
        if self.table[key] is not None:
            for item in self.table[key]:
                if item == k:
                    return True

            self.table[key].append(k)
        return False

    def delete(self, k):
        """
        Deletes an element from the has table if it exists
        """
        key = self.h(k)
        if self.table[key] is not None:
            i = 0
            for item in self.table[key]:
                if item is k:
                    self.table[key].pop(i)
                    self.num -= 1
                    return True
                i += 1

        return False

    def size(self):
        """
        Number of elements currently in hash table
        """
        return self.num


def testChainedHashTable():
    openTable = HashTableChaining(1000)
    openTable.insert("hello")
    openTable.insert("world")
    openTable.insert("this")
    openTable.insert("is")
    openTable.insert("paul")
    openTable.insert("paul")

    print(openTable.contains("paul"))
    print(openTable.contains("paulo"))

    openTable.delete("paul")
    print(openTable.contains("paul"))

    openTable.delete("paul")
    print(openTable.contains("paul"))


print("\nTesting Chaining Table\n")
testChainedHashTable()
