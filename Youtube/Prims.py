

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
        self.d = 9999
        self.pi = None

    def addUndirectedEdge(self, v, w):
        if not (v in self.edges):
            self.edges[v] = w
            v.addUndirectedEdge(self, w)

    def __repr__(self):
        return "\n\nnode: " + self.val + "\nd: " + str(self.d)


def Prims(vertices):
    vertices[0].d = 0

    heap = heapify(vertices)
    heap = heap[:]

    seen = set()
    while len(heap) > 0:
        cur = heap[0]
        seen.add(cur)

        for i in cur.edges:

            if not (i in seen):

                if cur.edges[i] < i.d:
                    i.d = cur.edges[i]
                    i.pi = cur

        heap[0] = heap[-1]
        heap.pop()
        heap = heapify(heap)

    return(vertices)



def buildGraph():
    a = node('a')
    b = node('b')
    c = node('c')
    d = node('d')
    e = node('e')
    f = node('f')

    a.addUndirectedEdge(b, 7)
    a.addUndirectedEdge(c, 1)
    b.addUndirectedEdge(f, 3)
    f.addUndirectedEdge(c, 1)
    f.addUndirectedEdge(d, 2)
    d.addUndirectedEdge(e, 2)
    c.addUndirectedEdge(e, 9)

    mst = (Prims([a, b, c, d, e, f]))

    for i in mst:
        print(i.val)
        print(i.d)
        if i.pi != None:
            print(i.pi.val)
        print()


# buildGraph()





