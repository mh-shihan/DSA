import heapq

class Solution:
    def spanningTree(self, V, edges):
        # Build adjacency list from edge list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # undirected graph

        vis = [0] * V
        pq = [(0, 0)]
        total = 0

        while pq:
            wt, node = heapq.heappop(pq)

            if vis[node] == 1:
                continue

            vis[node] = 1
            total += wt

            for adj_node, edge_w in adj[node]:
                if not vis[adj_node]:
                    heapq.heappush(pq, (edge_w, adj_node))

        return total