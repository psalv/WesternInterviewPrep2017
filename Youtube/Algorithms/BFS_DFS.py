
class node(object):
    def __init__(self, v):
        self.val = v
        self.edges = []
        self.d = 9999
        self.pi = None

    def addEdge(self, v):
        self.edges.append(v)

    def __repr__(self):
        return self.val


def BFS(root, end):
    seen = set()
    q = [root]

    while len(q) > 0:
        cur = q[0]
        q = q[1:]
        seen.add(cur)

        if cur.val == end:
            return True

        for i in cur.edges:
            if not (i in seen):
                q.append(i)
                i.pi = cur

    return False


def solveDFS(cur, end, seen):
    if cur.val == end:
        return True
    seen.add(cur)

    for i in cur.edges:
        if not (i in seen):
            i.pi = cur
            if solveDFS(i, end, seen):
                return True

    return False


def DFS(root, end):
    seen = set()

    if root.val == end:
        return True

    for i in root.edges:
        if not (i in seen):
            i.pi = root
            if solveDFS(i, end, seen):
                return True

    return False


def printPath(end):
    build = ""
    cur = end
    build += str(cur)
    while cur.pi != None:
        build += " <- " + str(cur.pi)
        cur = cur.pi

    print(build)
    print()

def buildGraph():
    a = node('a')
    b = node('b')
    c = node('c')
    d = node('d')
    e = node('e')
    f = node('f')

    a.addEdge(b)
    a.addEdge(c)
    b.addEdge(d)
    d.addEdge(f)
    c.addEdge(e)
    e.addEdge(f)


    print(BFS(a, "d"))
    printPath(d)

    print(BFS(b, "d"))
    printPath(b)


    print(BFS(b, "a"))
    print(BFS(a, "k"))




    print()

    print(DFS(a, "d"))
    printPath(d)


    print(DFS(b, "d"))
    printPath(b)


    print(DFS(b, "a"))
    print(DFS(a, "k"))


buildGraph()
