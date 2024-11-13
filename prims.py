import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t {self.graph[i][parent[i]]}")

    def minKey(self, key, mstSet):
        min = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min and not mstSet[v]:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

def inputGraph():
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)
    print("Enter the adjacency matrix (enter 0 for no connection):")
    for i in range(vertices):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        g.graph[i] = row
    return g

if __name__ == "__main__":
    g = inputGraph()
    g.primMST()
