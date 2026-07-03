graph = {
    'S': ({'A': 2, 'E': 3}, 6),
    'A': ({'S': 2, 'D': 1}, 3),
    'B': ({'C': 2, 'D': 3}, 2),
    'C': ({'B': 2, 'G': 3}, 2),
    'D': ({'A': 1, 'B': 3, 'G': 2}, 4),
    'E': ({'S': 3, 'G': 2}, 5),
    'G': ({}, 0)
}

def greedy_search_rec(graph, prev, dst, path, q):
    # Access neighbors from the first element of the tuple
    neighbors = graph[prev][0].keys()
    
    for n in neighbors:
        if n not in path:
            # Access heuristic from the second element of the tuple
            q[n] = graph[n][1]
            print(f"{n} -> {q[n]}")
            
    while q:
        mn = min(q, key=q.get)
        print(f"Taking minimum h(n) vertex: {mn}")
        
        if dst == mn:
            return path + [dst]
        
        current_node = mn
        del q[mn]
        
        new_path = greedy_search_rec(graph, current_node, dst, path + [current_node], q)
        if new_path:
            return new_path
            
    return []

# Execution
source=input("Enter Source Vertex:")
result = greedy_search_rec(graph,source, 'G',[source], {})
print("Resulting Path:", result)
