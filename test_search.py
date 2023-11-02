import unittest
import search

# [ -- PRUEBAS AUTOMÁTICAS -- ]

class TestSearchFunctions(unittest.TestCase): 
    def assertRouteCorrect(self, route, expected_nodes, visited, expected_visited, generated, expected_generated, cost, expected_cost):
        nodes = [node.state for node in route]
        self.assertEqual(nodes, expected_nodes, f"Ruta incorrecta: {nodes}")
        self.assertEqual(visited, expected_visited, f"Número incorrecto de nodos visitados: {visited}")
        self.assertEqual(generated, expected_generated, f"Número incorrecto de nodos generados: {generated}")
        self.assertEqual(cost, expected_cost, f"Costo incorrecto de la ruta: {cost}")

    def test_case_1(self):
        origin, destination = 'A', 'B'
        expected_routes = {
            'amplitud': ['B', 'F', 'S', 'A'],
            'profundidad': ['B', 'P', 'C', 'D', 'M', 'L', 'T', 'A'],
            'ramificacion_acotacion': ['B', 'P', 'R', 'S', 'A'],
            'ramificacion_acotacion_subestimacion': ['B', 'P', 'R', 'S', 'A']
        }
        expected_visited = {'amplitud': 16, 'profundidad': 10, 'ramificacion_acotacion': 24, 'ramificacion_acotacion_subestimacion': 6}
        expected_generated = {'amplitud': 21, 'profundidad': 18, 'ramificacion_acotacion': 31, 'ramificacion_acotacion_subestimacion': 16}
        expected_cost = {'amplitud': 450, 'profundidad': 733, 'ramificacion_acotacion': 418, 'ramificacion_acotacion_subestimacion': 418}
        self.run_test_case(origin, destination, expected_routes, expected_visited, expected_generated, expected_cost)
  
    def test_case_2(self):
        origin, destination = 'O', 'E'
        expected_routes = {
            'amplitud': ['E', 'H', 'U', 'B', 'F', 'S', 'O'],
            'profundidad': ['E', 'H', 'U', 'B', 'P', 'R', 'S', 'O'],
            'ramificacion_acotacion': ['E', 'H', 'U', 'B', 'P', 'R', 'S', 'O'],
            'ramificacion_acotacion_subestimacion': ['E', 'H', 'U', 'B', 'P', 'R', 'S', 'O']
        }
        expected_visited = {'amplitud': 43, 'profundidad': 31, 'ramificacion_acotacion': 40, 'ramificacion_acotacion_subestimacion': 15}
        expected_generated = {'amplitud': 45, 'profundidad': 41, 'ramificacion_acotacion': 43, 'ramificacion_acotacion_subestimacion': 32}
        expected_cost = {'amplitud': 730, 'profundidad': 698, 'ramificacion_acotacion': 698, 'ramificacion_acotacion_subestimacion': 698}
        self.run_test_case(origin, destination, expected_routes, expected_visited, expected_generated, expected_cost)

    def test_case_3(self):
        origin, destination = 'G', 'Z'
        expected_routes = {
            'amplitud': ['Z', 'A', 'S', 'F', 'B', 'G'],
            'profundidad': ['Z', 'A', 'T', 'L', 'M', 'D', 'C', 'P', 'R', 'S', 'F', 'B', 'G'],
            'ramificacion_acotacion': ['Z', 'A', 'S', 'R', 'P', 'B', 'G'],
            'ramificacion_acotacion_subestimacion': ['Z', 'A', 'S', 'R', 'P', 'B', 'G']
        }
        expected_visited = {'amplitud': 34, 'profundidad': 21, 'ramificacion_acotacion': 35, 'ramificacion_acotacion_subestimacion': 12}
        expected_generated = {'amplitud': 41, 'profundidad': 32, 'ramificacion_acotacion': 41, 'ramificacion_acotacion_subestimacion': 26}
        expected_cost = {'amplitud': 615, 'profundidad': 1284, 'ramificacion_acotacion': 583, 'ramificacion_acotacion_subestimacion': 583}
        self.run_test_case(origin, destination, expected_routes, expected_visited, expected_generated, expected_cost)

    def test_case_4(self):
        origin, destination = 'N', 'D'
        expected_routes = {
            'amplitud': ['D', 'C', 'P', 'B', 'U', 'V', 'I', 'N'],
            'profundidad': ['D', 'C', 'P', 'R', 'S', 'F', 'B', 'U', 'V', 'I', 'N'],
            'ramificacion_acotacion': ['D', 'C', 'P', 'B', 'U', 'V', 'I', 'N'],
            'ramificacion_acotacion_subestimacion': ['D', 'C', 'P', 'B', 'U', 'V', 'I', 'N']
        }
        expected_visited = {'amplitud': 26, 'profundidad': 19, 'ramificacion_acotacion': 26, 'ramificacion_acotacion_subestimacion': 12}
        expected_generated = {'amplitud': 32, 'profundidad': 31, 'ramificacion_acotacion': 32, 'ramificacion_acotacion_subestimacion': 23}
        expected_cost = {'amplitud': 765, 'profundidad': 1151, 'ramificacion_acotacion': 765, 'ramificacion_acotacion_subestimacion': 765}
        self.run_test_case(origin, destination, expected_routes, expected_visited, expected_generated, expected_cost)

    def test_case_5(self):
        origin, destination = 'M', 'F'
        expected_routes = {
            'amplitud': ['F', 'S', 'R', 'C', 'D', 'M'],
            'profundidad': ['F', 'B', 'P', 'R', 'S', 'A', 'T', 'L', 'M'],
            'ramificacion_acotacion': ['F', 'S', 'R', 'C', 'D', 'M'],
            'ramificacion_acotacion_subestimacion': ['F', 'S', 'R', 'C', 'D', 'M']
        }
        expected_visited = {'amplitud': 23, 'profundidad': 18, 'ramificacion_acotacion': 27, 'ramificacion_acotacion_subestimacion': 16}
        expected_generated = {'amplitud': 31, 'profundidad': 29, 'ramificacion_acotacion': 36, 'ramificacion_acotacion_subestimacion': 25}
        expected_cost = {'amplitud': 520, 'profundidad': 928, 'ramificacion_acotacion': 520, 'ramificacion_acotacion_subestimacion': 520}
        self.run_test_case(origin, destination, expected_routes, expected_visited, expected_generated, expected_cost)
    

    def run_test_case(self, origin, destination, expected_routes, expected_visited, expected_generated, expected_cost):
        gps = search.GPSProblem(origin, destination, search.romania)

        #--- Amplitud ---"
        route = search.breadth_first_graph_search(gps)[0].path()
        visited = search.breadth_first_graph_search(gps)[1]
        generated = search.breadth_first_graph_search(gps)[2]
        cost = search.breadth_first_graph_search(gps)[3]
        self.assertRouteCorrect(route, expected_routes['amplitud'], visited, expected_visited['amplitud'], generated, expected_generated['amplitud'], cost, expected_cost['amplitud'])

        #n--- Profundidad ---"
        route = search.depth_first_graph_search(gps)[0].path()
        visited = search.depth_first_graph_search(gps)[1]
        generated = search.depth_first_graph_search(gps)[2]
        cost = search.depth_first_graph_search(gps)[3]
        self.assertRouteCorrect(route, expected_routes['profundidad'], visited, expected_visited['profundidad'], generated, expected_generated['profundidad'], cost, expected_cost['profundidad'])

        #--- Ramificación y Acotación ---"
        route = search.branch_and_bound_search_estrategy(gps)[0].path()
        visited = search.branch_and_bound_search_estrategy(gps)[1]
        generated = search.branch_and_bound_search_estrategy(gps)[2]
        cost = search.branch_and_bound_search_estrategy(gps)[3]
        self.assertRouteCorrect(route, expected_routes['ramificacion_acotacion'], visited, expected_visited['ramificacion_acotacion'], generated, expected_generated['ramificacion_acotacion'], cost, expected_cost['ramificacion_acotacion'])

        #--- Ramificación y Acotación con Subestimación ---"
        route = search.branch_and_bound_search_estrategy_with_heuristics(gps)[0].path()
        visited = search.branch_and_bound_search_estrategy_with_heuristics(gps)[1]
        generated = search.branch_and_bound_search_estrategy_with_heuristics(gps)[2]
        cost = search.branch_and_bound_search_estrategy_with_heuristics(gps)[3]
        self.assertRouteCorrect(route, expected_routes['ramificacion_acotacion_subestimacion'], visited, expected_visited['ramificacion_acotacion_subestimacion'], generated, expected_generated['ramificacion_acotacion_subestimacion'], cost, expected_cost['ramificacion_acotacion_subestimacion'])

if __name__ == '__main__':
    unittest.main()
