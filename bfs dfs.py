def bfs(graph, start_node):
    visited = []
    queue = [start_node]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(graph[node])

graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter starting node for BFS: ")
print("Breadth-First Search:")
bfs(graph, start_node)

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

start_node = input("\nEnter the starting node for DFS: ")
print("Depth-First Search:")
dfs(visited, graph, start_node)
