print("krishna,192211408")
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_recursive(self, node, visited):
        visited.add(node)
        print(node, end=' ')

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start_node):
        visited = set()
        self.dfs_recursive(start_node, visited)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Depth-First Traversal (starting from vertex 2):")
    g.dfs(2)

