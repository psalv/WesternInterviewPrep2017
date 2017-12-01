

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


def propogateUndefined(v):
    if v.pi == "UND":
        return

    v.pi = "UND"
    for i in v.edges:
        propogateUndefined(i)


def bellmanFord(vertices, source):
    source.d = 0

    # initially relax all of the edges
    for i in vertices:
        for j in i.edges:
            relax(i, j, i.edges[j])

    # see if we can relax them any more, if so set as undefined
    for i in vertices:
        for j in i.edges:
            if j.d > j.d + i.edges[j]:
                propogateUndefined(j)

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
    g = node('g')

    a.addEdge(b, 1)
    a.addEdge(c, 10)
    b.addEdge(d, 3)
    b.addEdge(c, 1)
    d.addEdge(f, 3)
    c.addEdge(e, 10)
    e.addEdge(f, 1)
    f.addEdge(g, 1)     # should be undefined
    g.addEdge(f, -10)   # should be undefined

    bellmanFord([a, b, c, d, e, f, g], a)


buildGraph()
