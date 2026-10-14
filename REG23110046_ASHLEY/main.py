import sys
import heapq

"""
1) Uses a heap to get values in sorted descending order.
2) Adjacency matrix to store edge data as graph.
3) DFS to get connected components and their sizes.
4) Seen set to keep track of visited elements.
"""


def solver(n, m, e):
    
    def dfs(node):
        count = 0
        if node not in seen:
            seen[node] = True
            count += 1
            for nei in graph[node]:
                if not seen[nei]:
                    count += dfs(nei)
        return count
    
    graph = [[] for _ in range(n + 1)]
    
    for u, v in e:
        graph[u].append(v)
        graph[v].append(u)

    sizes = []
    components = 0
    seen = [False] * (n + 1)
    
    
    for node in range(1, n + 1):
        if not seen[node]:
            components += 1
            heapq.heappush(sizes, -(dfs(node)))
        
    print(components)
    while len(sizes) > 0:
        print(-heapq.heappop(sizes), end = " ")


if __name__ == "__main__":
    n = int(input()) # Number of nodes
    m = int(input()) # Number of edges
    edges = []
    for _ in range(m): # Iterate to get each edge
        x, _, y = list(input())
        if x is None or y is None or not x.isdigit() or not y.isdigit() or _ != " ":
            print("Invalid input!!!")
            sys.exit()
        edges.append([int(x), int(y)])
    solver(n, m, edges)