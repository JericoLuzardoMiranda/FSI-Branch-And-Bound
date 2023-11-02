import search

# [ -- PRUEBAS MANUALES -- ]

def search_route(number, origin, destination, graph):
    print(f"\n========== ID {number}: {origin} - {destination} ==========")
    gps = search.GPSProblem(origin, destination, graph)

    print("--- Amplitud ---")
    result_bfs = search.breadth_first_graph_search(gps)
    print(result_bfs[0].path(),"Visitados:",  result_bfs[1], ", Generados:", result_bfs[2], ", Coste Total:", result_bfs[3])

    print("\n--- Profundidad ---")
    result_dfs = search.depth_first_graph_search(gps)
    print(result_dfs[0].path(), "Visitados:", result_dfs[1], ", Generados:", result_dfs[2], ", Coste Total:", result_dfs[3])

    print("\n--- Ramificación y Acotación ---")
    result_BB = search.branch_and_bound_search_estrategy(gps)
    print(result_BB[0].path(), "Visitados:", result_BB[1], ", Generados:", result_BB[2], ", Coste Total:", result_BB[3])
    print("\n--- Ramificación y Acotación con Subestimación ---")
    result_BBH = search.branch_and_bound_search_estrategy_with_heuristics(gps)
    print(result_BBH[0].path(), "Visitados:", result_BBH[1], ", Generados:", result_BBH[2], ", Coste Total:", result_BBH[3])


search_route(1, 'A', 'B', search.romania)
search_route(2, 'O', 'E', search.romania)
search_route(3, 'G', 'Z', search.romania)
search_route(4, 'N', 'D', search.romania)
search_route(5, 'M', 'F', search.romania)
