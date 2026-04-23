from typing import List

class DisjointSet:
    def __init__(self, n):
        self.rank   = [0] * (n + 1)
        self.size   = [1] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    # PATH COMPRESSION
    def find_ult_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ult_parent(self.parent[node])
        return self.parent[node]

    # UNION BY RANK
    def union_by_rank(self, u, v):
        ulp_u = self.find_ult_parent(u)
        ulp_v = self.find_ult_parent(v)
        if ulp_u == ulp_v:
            return False
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
        return True

    # UNION BY SIZE
    def union_by_size(self, u, v):
        ulp_u = self.find_ult_parent(u)
        ulp_v = self.find_ult_parent(v)
        if ulp_u == ulp_v:
            return False
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v]  += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u]  += self.size[ulp_v]
        return True


class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: x[2])   # sort by weight  O(E log E)

        ds         = DisjointSet(V)
        mst_weight = 0
        mst_edges  = []

        for u, v, w in edges:           
            if ds.union_by_rank(u, v):
                mst_weight += w
                mst_edges.append((u, v, w))
                if len(mst_edges) == V - 1:
                    break

        return mst_weight