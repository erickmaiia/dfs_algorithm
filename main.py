from load_graph import load_graph
from print_result import print_result


def dfs_visit(u):
    global mark
    color[u] = "gray"
    mark += 1
    d[u] = mark

    for v in adj_list[u]:
        if color[v] == "white":
            edge_types[(u, v)] = "Arvore"
            dfs_visit(v)
        elif color[v] == "gray":
            edge_types[(u, v)] = "Retorno"
        else:
            if d[u] < d[v]:
                edge_types[(u, v)] = "Avanco"
            else:
                edge_types[(u, v)] = "Cruzamento"
    color[u] = "black"
    mark += 1
    f[u] = mark


def dfs():
    for u in v:
        if color[u] == "white":
            dfs_visit(u)


file_name = "G3.txt"
adj_list, high_degree, N = load_graph(file_name)
v = high_degree
color = ["white"] * N
d, f = [0] * N, [0] * N
edge_types, mark = {}, 0
dfs()
print_result(d, f, edge_types)
