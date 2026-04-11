from collections import deque

def bfsOfGraph( adj):
    V = len(adj)
    vis = [0] * V
    vis[0] = 1
    
    q = deque()
    q.append(0)
    
    bfs = []
    
    while q:
        node = q.popleft()
        bfs.append(node)
        
        for i in adj[node]:
            if not vis[i]:
                vis[i] = 1
                q.append(i)
    
    return bfs