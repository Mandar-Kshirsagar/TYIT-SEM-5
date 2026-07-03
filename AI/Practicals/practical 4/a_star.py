graph ={
    "a":({"b":1, "d":2, "e":3},4),
    "b":({"c":2, "d":1},3),
    "c":({"f":3},2),
    "d":({"f":2},3),
    "e":({"d":3, "f":4},2),
    "f":({},0)
    }
def a_star(graph, prev, dst, path, pcost, q):
    print("connected nodes of current node", prev,"with h(n) values:")
    for n in graph[A][0]:
        if n not in path:
            q[n] = (graph[n][1], graph[prev][O][n])
            print(n,"->",q[n])
        while q:
            mn = min(q, key=q.get)
            print("Taking minimum h(n) vertex:", mn)
            if dst == mn:
                return path + [dst]
            new_path = greedy_search_rec(graph, mn, dst, path + [mn],q)
            if new_path:
                return new_path
            return []

source=input("Enter source vertex: ")
dest=input("Enter destination vertex:")
path=a_star(graph, source, dest, [source],{})

if path:
    print(path)
else:
    print("path not found:")
