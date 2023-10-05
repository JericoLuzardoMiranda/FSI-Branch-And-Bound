# Search methods

import search

print("=== ID 1: Arad - Bucharest ===")
ab = search.GPSProblem('A', 'B', search.romania)

print("--- Amplitud ---")
print(search.breadth_first_graph_search(ab).path())

print("\n--- Profundidad ---")
print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

print("\n=== ID 2: Oradea - Eforie ===")
oe = search.GPSProblem('O', 'E', search.romania)

print("--- Amplitud ---")
print(search.breadth_first_graph_search(oe).path())

print("\n--- Profundidad ---")
print(search.depth_first_graph_search(oe).path())

print("\n=== ID 3: Giurgiu - Zerind ===")
gz = search.GPSProblem('G', 'Z', search.romania)

print("--- Amplitud ---")
print(search.breadth_first_graph_search(gz).path())

print("\n--- Profundidad ---")
print(search.depth_first_graph_search(gz).path())

print("\n=== ID 4: Neamt - Dobreta ===")
nd = search.GPSProblem('N', 'D', search.romania)

print("--- Amplitud ---")
print(search.breadth_first_graph_search(nd).path())

print("\n--- Profundidad ---")
print(search.depth_first_graph_search(nd).path())

print("\n=== ID 5: Mehadia - Fagaras ===")
mf = search.GPSProblem('M', 'F', search.romania)

print("--- Amplitud ---")
print(search.breadth_first_graph_search(mf).path())

print("\n--- Profundidad ---")
print(search.depth_first_graph_search(mf).path())
