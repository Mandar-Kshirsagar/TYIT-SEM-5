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

def dfs(g, n, seen, d):
    if n not in seen:
        seen.append(n)
        for i in g[n]:
            if seen[-1] is d:
                break
            dfs(g, i, seen, d)
    return seen

print(dfs(graph, 'A', [], 'H'))
