def print_result(d, f, edge_types):
    for (exit_degree, entry_grade), edge_type in edge_types.items():
        print(f"{exit_degree} {entry_grade}: {edge_type}")

    print(f"d vector : {d}")
    print(f"f vector : {f}")
