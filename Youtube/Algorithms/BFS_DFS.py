
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
    seen.add(root)
    q = [root]

    while len(q) > 0:
        cur = q[0]
        q = q[1:]

        if cur.val == end:
            return True

        for i in cur.edges:
            if not (i in seen):
                seen.add(i)
                q.append(i)
                i.pi = cur

    return False


def dfsVisit(cur, search, seen):
    seen.add(cur)

    if cur.val == search:
        return cur

    for v in cur.edges:
        if not (v in seen):
            v.pi = cur
            ans = dfsVisit(v, search, seen)
            if ans is not False:
                return ans

    return False


def dfs(cur, search):
    seen = set()
    return dfsVisit(cur, search, seen)


def printPath(end):
    build = ""
    cur = end
    build += str(cur)
    while cur.pi is not None:
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

    print(not BFS(b, "a"))
    print(not BFS(a, "k"))

    print()

    print(dfs(a, "d"))
    printPath(d)

    print(dfs(b, "d"))
    printPath(b)

    print(not dfs(b, "a"))
    print(not dfs(a, "k"))


buildGraph()
