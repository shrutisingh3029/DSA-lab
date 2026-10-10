# Road Network using Adjacency Matrix and DFS

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[0] * n for i in range(n)]
        self.visited = [0] * n

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def DFS(self, v):
        print(v, end=" ")
        self.visited[v] = 1

        i = 0
        while i < self.n:
            if self.graph[v][i] == 1 and self.visited[i] == 0:
                self.DFS(i)
            i = i + 1


# Main program

n = int(input("Enter number of intersections: "))

g = Graph(n)

e = int(input("Enter number of roads: "))

i = 0
while i < e:
    u = int(input("Enter first intersection: "))
    v = int(input("Enter second intersection: "))

    g.add_edge(u, v)

    i = i + 1

start = int(input("Enter starting intersection: "))

print("DFS Traversal: ", end="")
g.DFS(start)
print()