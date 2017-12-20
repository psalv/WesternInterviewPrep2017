
import sys


def minheapifyD(ar, i):

    l = 2 * i + 1
    r = 2 * i + 2

    if l >= len(ar):
        return

    smallest = i
    if ar[l].d < ar[i].d:
        smallest = l

    if r < len(ar) and ar[r].d < ar[smallest].d:
        smallest = r

    if smallest != i:
        temp = ar[i]
        ar[i] = ar[smallest]
        ar[smallest] = temp

        minheapifyD(ar, smallest)


def heapify(ar):
    for i in range(len(ar) // 2 + 1, -1, -1):
        minheapifyD(ar, i)
    return ar


class node(object):
    def __init__(self, v):
        self.val = v
        self.edges = {}
        self.d = sys.maxsize
        self.pi = None

    def addEdge(self, v, w):
        self.edges[v] = w

    def __repr__(self):
        return self.val


def relax(u, v, z):
    if v.d > u.d + z:
        v.d = u.d + z
        v.pi = u
        return True

    return False


def dijkstra(vertices, root):
    seen = set()
    root.d = 0

    heap = heapify(vertices[:])

    while len(heap) > 0:
        cur = heap[0]
        seen.add(cur)

        heap[0] = heap[-1]
        heap.pop()
        for e in cur.edges:
            if not (e in seen):
                relax(cur, e, cur.edges[e])

        heap = heapify(heap)
        # minheapifyD(heap, 0)

    for i in vertices:
        print()
        print(i)
        print("d:  ", i.d)
        print("pi: ", i.pi)


def buildGraph():
    a = node('a')
    b = node('b')
    c = node('c')
    d = node('d')
    e = node('e')
    f = node('f')

    a.addEdge(b, 1)
    a.addEdge(c, 10)
    b.addEdge(d, 3)
    b.addEdge(c, 1)
    d.addEdge(f, 3)
    c.addEdge(e, 10)
    e.addEdge(f, 1)

    dijkstra([a, b, c, d, e, f], a)


buildGraph()
