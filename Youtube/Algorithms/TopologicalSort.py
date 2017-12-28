
import sys

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


def TopologicalSort(vertices):
    """
    We only add vertices to the sort once their in degree is zero (decrementing each time we traverse an edge to it)
    Does not check for cycles (assumes it is acyclic), can easily check this by keeping a set of everything already sorted.
    This algorithm will be O(|V| + |E|) time and O(|V|) space, both of which are the best that can occur.
    """
    inDegrees = {}

    # O(|E|) time since we build in degrees from each edge
    for v in vertices:
        if v not in inDegrees:
            inDegrees[v] = 0
        for e in v.edges:
            if e not in inDegrees:
                inDegrees[e] = 1
            else:
                inDegrees[e] += 1

    # O(|V|) time since we are building the Q
    Q = []
    for i in inDegrees:
        if inDegrees[i] == 0:
            Q.append(i)

    # We iterate through every edge, adding always to the back of the list and never popping from the front
    # So the is O(|E|) iterations, and will take up O(|V|) extra space.
    pos = 0
    sort = []
    while pos < len(Q):
        cur = Q[pos]
        pos += 1
        sort.append(cur)
        for e in cur.edges:
            inDegrees[e] -= 1
            if inDegrees[e] == 0:
                Q.append(e)

    return sort


def buildGraph():
    a = node('a')
    b = node('b')
    c = node('c')
    d = node('d')
    e = node('e')
    f = node('f')
    g = node('g')

    a.addEdge(b, 1)
    a.addEdge(c, 1)
    b.addEdge(c, 1)
    b.addEdge(f, 1)
    c.addEdge(d, 1)
    d.addEdge(f, 1)
    f.addEdge(e, 1)

    print(TopologicalSort([d, e, f, a, g, c, b]))


buildGraph()
