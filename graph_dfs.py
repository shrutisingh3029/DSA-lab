# Graph using Adjacency Matrix and DFS

n = int(input("Enter number of vertices: "))

graph = [[0] * n for i in range(n)]

e = int(input("Enter number of edges: "))

i = 0
while i < e:
    u = int(input("Enter starting vertex: "))
    v = int(input("Enter ending vertex: "))

    graph[u][v] = 1
    graph[v][u] = 1

    i = i + 1


visited = [0] * n

def DFS(v):
    print(v, end=" ")
    visited[v] = 1

    i = 0
    while i < n:
        if graph[v][i] == 1 and visited[i] == 0:
            DFS(i)

        i = i + 1


start = int(input("Enter starting vertex for DFS: "))

print("DFS Traversal:", end=" ")
DFS(start)