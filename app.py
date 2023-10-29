# Carregamento do arquivo

def load_list():
    file = open("GD1.txt", "r")
    listt = file.readlines()
    for i in range(len(listt)):
        line = listt[i].split()
        if i == 0:
            N = int(line[0])
            adj_list = [[] for _ in range(N)]
        else:
            adj_list[int(line[0]) - 1].append(int(line[1]) - 1)
    file.close()
    return adj_list, N

# Algoritmo de visita DFS

def dfs_visit(u):
    global mark
    color[u] = "gray"
    mark += 1
    d[u] = mark
    for v in adj_list[u]:
        if color[v] == "white":
            dfs_visit(v)
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
    print(f"d vector : {d}")
    print(f"f vector : {f}")


adj_list, N = load_list()
v = [1,2,3,4,5,6,0,7] # Ordem de incialização do DFS pelo zero | Nesse exemplo ele começa do sexto indice
color = ["white"] * N
d = [0] * N
f = [0] * N
mark = 0
dfs()
print_list(d, f)
