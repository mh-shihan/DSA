n, m = map(int, input().split())

adj_matrix = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1 # As it is an undirected graph

# Print adjacency matrix
for i in range(1, n+1):
    for j in range(1, n+1):
        print(adj_matrix[i][j], end=" ")
    print()