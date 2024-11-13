def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}
    
    while open_set:
        n = None
        
        for v in open_set:
            if n is None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print("Path found:", path)
            return path

        open_set.remove(n)
        closed_set.add(n)

        for (m, weight) in graph[n]:
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            elif g[m] > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n

    print("Path does not exist!")
    return None

graph = {}
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors and weights (e.g., B,6 C,2): ").split()
    graph[node] = [(neighbor.split(",")[0], int(neighbor.split(",")[1])) for neighbor in neighbors]

heuristic = {}
for _ in range(n):
    node = input("Enter node: ")
    heuristic[node] = int(input(f"Enter heuristic value for {node}: "))

start_node = input("Enter the start node: ")
stop_node = input("Enter the goal node: ")

aStarAlgo(start_node, stop_node)
