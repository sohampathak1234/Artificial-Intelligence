class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def is_safe(self, v, color, colors):
        for i in range(self.vertices):
            if self.adj_matrix[v][i] == 1 and colors[i] == color:
                return False
        return True

    def graph_coloring_util(self, num_colors, colors, v):
        if v == self.vertices:
            return True

        for color in range(1, num_colors + 1):
            if self.is_safe(v, color, colors):
                colors[v] = color
                if self.graph_coloring_util(num_colors, colors, v + 1):
                    return True
                colors[v] = 0

        return False

    def graph_coloring(self, num_colors):
        colors = [0] * self.vertices

        if not self.graph_coloring_util(num_colors, colors, 0):
            print("No solution exists.")
        else:
            print("Graph coloring solution:")
            for v in range(self.vertices):
                print(f"Vertex {v + 1} -> Color {colors[v]}")


# Get the graph details from the user
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

graph = Graph(num_vertices)

print("Enter the edges in the format 'u v', where u and v are vertices connected by an edge:")
for _ in range(num_edges):
    u, v = map(int, input().split())

    # Validate the vertices entered
    if u < 1 or u > num_vertices or v < 1 or v > num_vertices:
        print("Invalid vertex entered. Please try again.")
        exit(1)

    graph.add_edge(u - 1, v - 1)

num_colors = int(input("Enter the number of colors available: "))

# Solve the graph coloring problem
graph.graph_coloring(num_colors)
