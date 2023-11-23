from collections import Counter


def load_graph(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    exit_degrees = []
    N_VERTEX = int(lines[0].split()[0])
    N_EDGES = int(lines[0].split()[1])
    ascii_a = ord('a')
    if N_EDGES <= 0:
        print("Grafo vazio")
        return exit(0)
    adj_list = [[] for _ in range(N_VERTEX)]  # List comprehension

    for line in lines[1:]:
        vertex1, vertex2 = line.split()
        if vertex1.isalpha() and vertex2.isalpha():
            # Ocorre um erro se o label não estiver em ordem consecutiva
            vertex1, vertex2 = ord(vertex1) - ascii_a, ord(vertex2) - ascii_a
            exit_degrees.append(vertex1)
            adj_list[vertex1].append(vertex2)
        else:
            vertex1, vertex2 = int(vertex1), int(vertex2)
            exit_degrees.append(int(line[0]))
            adj_list[vertex1].append(vertex2)

    count_degrees = Counter(exit_degrees)
    most_count_degree = count_degrees.most_common()
    high_degree = [element for element, _ in most_count_degree]

    return adj_list, high_degree, N_VERTEX
