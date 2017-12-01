

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
    def __init__(self, v):
        self.val = v
        self.edges = {}
        self.d = 999
        self.pi = None

    def addEdge(self, v, w):
        self.edges[v] = w

    def __repr__(self):
        return self.val


def relax(u, v, w):
    cur = v.d

    if cur == 999 or cur > u.d + w:
        v.d = u.d + w
        v.pi = u
        return True

    return False


# This is an all end points single source shortest path detection problem
# Meaning that you give the source and all of the connected components will have their
# d values set to the minimum one can traverse them to
def dijkstra(vertices, source):
    source.d = 0
    heap = heapify(vertices)
    heap = heap[:]

    seen = set()
    while len(heap) > 0:
        cur = heap[0]
        seen.add(cur)

        heap[0] = heap[-1]
        heap.pop()
        for i in cur.edges:
            if not (i in seen):
                relax(cur, i, cur.edges[i])

        if len(heap) > 1:
            heap = heapify(heap)

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
