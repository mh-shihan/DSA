
def dfsHelper(self, node, adj, vis, ans):
    vis[node] = 1
    ans.append(node)
    
    # traverse all its neighbours
    for i in adj[node]:
        if not vis[i]:
            self.dfsHelper(i, adj, vis, ans)

def dfs(self, adj):
    V = len(adj)
    vis = [0]*V
    ans = []
    start = 0
    
    self.dfsHelper(start, adj, vis, ans)
    return ans
    
        