# self.parent = list(range(n + 1))

class DisjointSet: 
    def __init__(self, n):
        self.rank = [0]*(n +1)
        self.size = [1]*(n + 1)
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

        if(ulp_u == ulp_v):
            return
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    # UNION BY SIZE
    def union_by_size(self, u, v): 
        ulp_u = self.find_ult_parent(u)
        ulp_v = self.find_ult_parent(v)

        if(ulp_u == ulp_v):
            return
        
        if(self.size[ulp_u] < self.size[ulp_v]):
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


# Example usage
ds = DisjointSet(7)
ds.union_by_rank(1, 2)
ds.union_by_rank(2, 3)
ds.union_by_rank(4, 5)
ds.union_by_rank(6, 7)
ds.union_by_rank(5, 6)

if ds.find_ult_parent(3) == ds.find_ult_parent(7):
    print("Same")
else:
    print("Not same")

ds.union_by_rank(3, 7)

if ds.find_ult_parent(3) == ds.find_ult_parent(7):
    print("Same")
else:
    print("Not same")