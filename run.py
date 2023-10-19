# Search methods
import search

def search_route(number, origin, destination, graph):
    print(f"\n========== ID {number}: {origin} - {destination} ==========")
    gps = search.GPSProblem(origin, destination, graph)

    print("--- Amplitud ---")
    print(search.breadth_first_graph_search(gps).path())

    print("\n--- Profundidad ---")
    print(search.depth_first_graph_search(gps).path())

    print("\n--- Ramificación y Acotación ---")
    print(search.branch_and_bound_search_estrategy(gps).path())

    print("\n--- Ramificación y Acotación con Subestimación ---")
    print(search.branch_and_bound_search_estrategy_with_heuristics(gps).path())


search_route(1, 'A', 'B', search.romania)
search_route(2, 'O', 'E', search.romania)
search_route(3, 'G', 'Z', search.romania)
search_route(4, 'N', 'D', search.romania)
search_route(5, 'M', 'F', search.romania)
