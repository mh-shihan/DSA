
n, m = map(int, input("Enter number of nodes and edges: ").split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    u, v, w = map(int, input("Enter u, v, weight: ").split())

    graph[u].append((v, w))
    graph[v].append((u, w))   # remove this line if graph is directed

# Print adjacency list
for vertex in graph:
    print(vertex, ":", graph[vertex])