from collections import Counter

def load_list(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    exit_degrees = []
    N = int(lines[0].split()[0])
    adj_list = [[] for _ in range(N)]

    for line in lines[1:]:
        vertex1, vertex2 = line.split()
        vertex1, vertex2 = ord(vertex1) - ord('a'), ord(vertex2) - ord('a')
        adj_list[vertex1].append(vertex2)
        exit_degrees.append(ord(line[0]) - ord('a'))

    count_degrees = Counter(exit_degrees)
    high_degree = [element for element, _ in count_degrees.most_common()]

    return adj_list, high_degree, N

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
            edge_types[(u, v)] = "Avanco" if d[u] < d[v] else "Cruzamento"

    color[u] = "black"
    mark += 1
    f[u] = mark

def dfs():
    for u in v:
        if color[u] == "white":
            dfs_visit(u)

def print_list():
    ascii_a = 97
    for (exit_degree, entry_grade), edge_type in edge_types.items():
        exit_degree, entry_grade = chr(exit_degree + ascii_a), chr(entry_grade + ascii_a)
        print(f"{exit_degree} {entry_grade}: {edge_type}")

    print(f"d vector : {d}")
    print(f"f vector : {f}")

file_name = "G1.txt"
adj_list, high_degree, N = load_list(file_name)
v = high_degree  # Order of initialization for DFS based on highest degree
color = ["white"] * N
d, f = [0] * N, [0] * N
edge_types, mark = {}, 0
dfs()
print_list()
