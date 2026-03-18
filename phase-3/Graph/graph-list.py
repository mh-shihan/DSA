
# graph.setdefault(u, []).append(v)
# graph.setdefault(v, []).append(u)

n, m = map(int, input().split())

graph = {}

for _ in range(m):
    u, v = map(int, input().split())

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)   # remove this line if graph is directed

# Print adjacency list
for vertex in graph:
    print(vertex, ":", graph[vertex])