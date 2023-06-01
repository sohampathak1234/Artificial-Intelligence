class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    
    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))

g = Graph(int(input("Enter the number of vertices in the graph: ")))

while True:
    edge = input("Enter an edge in the format 'u v weight' (or 'done' to finish): ")
    if edge == 'done':
        break
    else:
        u, v, w = map(int, edge.split())
        g.add_edge(u, v, w)

g.kruskal_mst()
