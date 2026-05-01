import heapq

# Time complexity: O(E log V) where E is the number of edges and V is the number of vertices

class Solution:
    def dijkstra(self, V, edges, src):
        # Build adjacency dictionary
        adj = {i: [] for i in range(V)}
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # undirected graph
        
        dist = [1e9] * V
        dist[src] = 0
        pq = [(0, src)]
        
        while pq:
            dis, node = heapq.heappop(pq)
            
            for adj_node, edge_weight in adj[node]:
                if dis + edge_weight < dist[adj_node]:
                    dist[adj_node] = dis + edge_weight
                    heapq.heappush(pq, (dist[adj_node], adj_node))
        
        return dist