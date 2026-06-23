import collections
def bfs(graph, root):
    seen, queue= set([root]),collections.deque([root])

    while queue:
        vertex = queue.popleft()
        visit(vertex)

        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

def allpath(st, end, gr):
    todo = [(st, [st])]

    while todo:
        node, path = todo.pop(0)

        for next_node in gr[node]:
            if next_node in path:
                continue
                print("ideal solution")
            if next_node == end:
                return path + [next_node]
            else:
                todo.append((next_node, path + [next_node]))
def visit(n):
    print(n)

def bfs_shortest_path(graph, source, destination):
    checked = []
    queue = [[source]]

    if source == destination:
        return [source]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in checked:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == destination:
                    return new_path

            checked.append(node)

    return "PATH DOES NOT EXIST"

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G', 'H'],
    'D': ['F'],
    'E': ['B', 'F'],
    'F': ['A'],
    'G': ['E', 'H'],
    'H': ['A']
}

print("GRAPH TRAVERSAL:")
bfs(graph, 'A')

print("\nAll paths:")
for x in allpath('A', 'E', graph):
    print(x)

print("\nSHORTEST PATH OF GRAPH IS:", bfs_shortest_path(graph, 'A', 'E'))