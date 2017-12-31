
from sys import maxsize


def heapify(ar):

    def minheapifyD(ar, i):

        l = 2 * i + 1
        r = 2 * i + 2

        if l >= len(ar):
            return ar

        smallest = i
        if ar[l].d < ar[i].d:
            smallest = l

        if r < len(ar) and ar[r].d < ar[smallest].d:
            smallest = r

        if smallest != i:
            temp = ar[i]
            ar[i] = ar[smallest]
            ar[smallest] = temp

            return minheapifyD(ar, smallest)

        else:
            return ar

    for i in range(len(ar) - 1, -1, -1):
        ar = minheapifyD(ar, i)
    return ar


class node(object):

    def __init__(self, val):
        self.val = val
        self.edges = []
        self.d = maxsize

    def __repr__(self):
        t = ""
        for i in self.edges:
            t += "\n\t-> " + str(i.val)
        return str(self.val) + t


def buildGraph(nodes):
    file = open("matrix.txt", "r")

    pos = 0
    for line in file:
        line = line.rstrip().split(",")
        pos = len(line)
        for i in range(len(line)):
            nodes.append(node(-1 * int(line[i])))

    return pos


def relax(u, v, z):
    if v.d > u.d + z:
        v.d = u.d + z
        v.pi = u
        return True

    return False


def findSum():
    nodes = []
    pos = buildGraph(nodes)
    counter = 0
    for i in range(len(nodes)):
        counter += 1
        if counter != pos:
            nodes[i].edges.append(nodes[i + 1])
        else:
            counter = 0

        if i + pos < len(nodes):
            nodes[i].edges.append(nodes[i + pos])

    seen = set()
    nodes[0].d = 0

    heap = heapify(nodes[:])

    while len(heap) > 0:
        cur = heap[0]
        seen.add(cur)

        heap[0] = heap[-1]
        heap.pop()
        for e in cur.edges:
            if not (e in seen):
                relax(cur, e, e.val)

        heap = heapify(heap)

    return -1 * nodes[-1].d


print(findSum())
