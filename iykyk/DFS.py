visited = []
stack = []

def dfs(graph, visited, start):
    visited.append(start)
    stack.append(start)
    print(start)

    while stack:
        m = stack[-1]
        found_unvisited_neighbour = False

        for adjacent in graph[m]:
            if adjacent not in visited:
                visited.append(adjacent)
                stack.append(adjacent)
                print(adjacent)
                found_unvisited_neighbour = True
                break

        if not found_unvisited_neighbour:
            stack.pop()

graph = {}
n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1}: ")
    neighbours = input("Enter the neighbours separated by a space: ").split()
    graph[node] = neighbours

start = input("Enter the starting vertex: ")
print("DFS result:")
dfs(graph, visited, start)
