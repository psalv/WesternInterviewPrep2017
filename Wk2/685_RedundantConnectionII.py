class Node(object):

    def __init__(self, val):
        self.val = val
        self.edges = []

    def addEdge(self, e):
        self.edges.append(e)

    def __repr__(self):
        return str(self.val)


class Graph(object):

    def __init__(self, edges):
        self.nodes = {}
        for e in edges:
            if e[0] not in self.nodes:
                self.nodes[e[0]] = Node(e[0])
            if e[1] not in self.nodes:
                self.nodes[e[1]] = Node(e[1])
            self.nodes[e[0]].addEdge(self.nodes[e[1]])

    def getNodes(self):
        return self.nodes


class QueueNode(object):

    def __init__(self, item):
        self.next = None
        self.item = item


class Solution(object):

    # Uses a modified BFS to check for redundant connection
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodes = Graph(edges).getNodes()
        total = len(nodes)

        startingPoints = set()

        for e in edges:

            if e[0] in startingPoints:
                continue
            else:
                startingPoints.add(e[0])

            # The current candidate root node
            root = nodes[e[0]]

            # A queue to to be used for a modified BFS
            queueFront = QueueNode(root)
            queueBack = queueFront

            seen = set()
            seen.add(root)

            redundant = None

            # We continue until there are no nodes from which to be
            while queueFront is not None:

                for neighbor in queueFront.item.edges:

                    if neighbor in seen:
                        redundant = neighbor.val

                    else:
                        seen.add(neighbor)
                        queueBack.next = QueueNode(neighbor)
                        queueBack = queueBack.next

                # Pop off the first element of the queue
                queueFront = queueFront.next

            # If all items were visited and there was a redundant edge
            if len(seen) == total and redundant is not None:

                # Start from the right
                # Remove an edge and see if everything is still connected.

                for edgeIndex in range(len(edges) - 1, -1, -1):
                    if edges[edgeIndex][1] == redundant:
                        currentEdge = edges[edgeIndex]

                        nodes[currentEdge[0]].edges.remove(nodes[currentEdge[1]])

                        if self.isComplete(root, total):
                            return currentEdge

                        else:
                            nodes[currentEdge[0]].edges.append(nodes[currentEdge[1]])
        return None


    def isComplete(self, root, total):

        queueFront = QueueNode(root)
        queueBack = queueFront

        seen = set()
        seen.add(root)

        while queueFront is not None:

            for neighbor in queueFront.item.edges:

                if neighbor not in seen:
                    seen.add(neighbor)
                    queueBack.next = QueueNode(neighbor)
                    queueBack = queueBack.next

            queueFront = queueFront.next

        return len(seen) == total


def test():
    test = [[1, 2], [1, 3], [2, 3]]
    # test = [[5,2],[5,1],[3,1],[3,4],[3,5]]
    print(Solution.findRedundantDirectedConnection(Solution(), test))

test()