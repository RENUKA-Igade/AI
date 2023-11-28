def bfs(visited, graph, node):
    visited.append(node)
    queue = [node]

    while queue:
        s = queue.pop(0)
        print(s, end=" ")  # Print the visited node

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Create a graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # List to keep track of visited nodes.

# Driver Code
bfs(visited, graph, 'A')
