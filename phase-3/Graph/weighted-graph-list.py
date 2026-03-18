
n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))   # remove this line if graph is directed

# Print adjacency list
for vertex in graph:
    print(vertex, ":", graph[vertex])