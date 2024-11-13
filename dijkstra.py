class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min = float('inf')
        min_index = -1
        for v in range(self.V):
            if dist[v] < min and not sptSet[v]:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if (self.graph[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        
        self.printSolution(dist)

def inputGraph():
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)
    edges = int(input("Enter the number of edges: "))
    
    for _ in range(edges):
        while True:
            user_input = input("Enter edge (u v w): ").strip()
            # Skip empty input
            if not user_input:
                print("Input cannot be empty. Please enter the edge in the format (u v w).")
                continue

            values = user_input.split()
            if len(values) != 3:
                print("Invalid input. Please enter exactly 3 values (u v w) separated by spaces.")
                continue

            try:
                u, v, w = map(int, values)
                if u < 0 or v < 0 or w < 0:
                    print("Vertex and weight values should be non-negative integers.")
                    continue
                g.graph[u][v] = w
                g.graph[v][u] = w
                break  # Exit the loop after successful input
            except ValueError:
                print("Invalid input. Please enter three integers (u v w) separated by spaces.")

    return g

if __name__ == "__main__":
    g = inputGraph()
    src = int(input("Enter the source vertex: "))
    g.dijkstra(src)
