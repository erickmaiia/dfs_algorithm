# Carregamento dos dados do arquivo

def load_list():
    file = open("GD.txt", "r")
    listt = file.readlines()
    N = int(listt[0].split()[0])
    adj_list = [[] for _ in range(N)]
    degree = []
    global boot_order

    for i in range(1, len(listt)):
        line = listt[i].split()
        vertex1, vertex2 = line  
        vertex1 = ord(vertex1) - ord('a')
        vertex2 = ord(vertex2) - ord('a')
        degree.append(vertex1)
        adj_list[vertex1].append(vertex2)
    
    file.close()
    print(degree)
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
v = [] # Ordem de incialização do DFS pelo zero/vertice com maior grau | Nesse exemplo ele começa do sexto indice
color = ["white"] * N
d = [0] * N
f = [0] * N
mark = 0
dfs()
print_list(d, f)
