from collections import deque
import time

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes_expanded


# ---------------- DFS ----------------
def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


# ---------------- Profiling ----------------
start = time.perf_counter()
bfs_nodes = bfs(graph, 'A', 'G')
bfs_time = (time.perf_counter() - start) * 1000

start = time.perf_counter()
dfs_nodes = dfs(graph, 'A', 'G')
dfs_time = (time.perf_counter() - start) * 1000


# ---------------- Results ----------------
print("BFS Results")
print("Time:", bfs_time, "ms")
print("Nodes Expanded:", bfs_nodes)

print("\nDFS Results")
print("Time:", dfs_time, "ms")
print("Nodes Expanded:", dfs_nodes)