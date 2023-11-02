import unittest
import search

class TestSearchFunctions(unittest.TestCase):
    def assertRouteCorrect(self, route, expected_nodes):
        nodes = [node.state for node in route]
        self.assertEqual(nodes, expected_nodes, f"Ruta incorrecta: {nodes}")

    def test_search_route(self):
        # Caso A-B
        print("\n========== ID 1: A - B ==========")
        origin = 'A'
        destination = 'B'
        gps = search.GPSProblem(origin, destination, search.romania)

        print("--- Amplitud ---")
        route = search.breadth_first_graph_search(gps).path()
        self.assertRouteCorrect(route, ['B', 'F', 'S', 'A'])

        print("\n--- Profundidad ---")
        route = search.depth_first_graph_search(gps).path()
        self.assertRouteCorrect(route, ['B', 'P', 'C', 'D', 'M', 'L', 'T', 'A'])

        print("\n--- Ramificación y Acotación ---")
        route = search.branch_and_bound_search_estrategy(gps).path()
        self.assertRouteCorrect(route, ['B', 'P', 'R', 'S', 'A'])

        print("\n--- Ramificación y Acotación con Subestimación ---")
        route = search.branch_and_bound_search_estrategy_with_heuristics(gps).path()
        self.assertRouteCorrect(route, ['B', 'P', 'R', 'S', 'A'])

if __name__ == '__main__':
    unittest.main()
