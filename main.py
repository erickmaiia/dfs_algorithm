from collections import Counter

# Carregamento do arquivo

def load_list():
    file = open("GD.txt", "r")
    listt = file.readlines()
    exit_degrees = []
    for i in range(len(listt)):
        line = listt[i].split()
        if i == 0:
            N = int(line[0])
            adj_list = [[] for _ in range(N)]
        else:
            vertex1, vertex2 = line 
            vertex1 = ord(vertex1) - ord('a')
            vertex2 = ord(vertex2) - ord('a')
            adj_list[vertex1].append(vertex2)
            exit_degrees.append(ord(line[0]) - ord('a'))
    count_degrees = Counter(exit_degrees)
    high_degree = [element for element, _ in count_degrees.most_common()]
    file.close()
    return adj_list, high_degree, N

# Algoritmo de visita DFS

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

# Algoritmo DFS

def dfs():
    for u in v:
        color[u] = "white"
    for u in v:
        if color[u] == "white":
            dfs_visit(u)

# Visualização dos dados

def print_list(d, f):
    for edge in edge_types.items():
        exit_degree = chr(edge[0][0] + 97)
        entry_grade = chr(edge[0][1] + 97)
        print(f"{exit_degree} {entry_grade}: {edge[1]}")
    print(f"d vector : {d}")
    print(f"f vector : {f}")


adj_list, high_degree, N = load_list()
v = high_degree # Ordem de incialização do DFS pelo maior grau
color = ["white"] * N
d = [0] * N
f = [0] * N
edge_types = {}
mark = 0
dfs()
print_list(d, f)
