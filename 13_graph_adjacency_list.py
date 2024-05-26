from collections import defaultdict
from collections import deque  # this will be our queue

class Graph:
	def __init__(self, Nodes=None, is_directed=True):
		self.nodes = Nodes
		self.is_directed = is_directed
		self.adj_list = defaultdict(list)

		if self.nodes:
			for node in self.nodes:
				self.adj_list[node] = []

	def add_edge(self, src, des):
		self.adj_list[src].append(des)

		if self.is_directed == False:
			self.adj_list[des].append(src)

	def print_list(self):
		for key, val in self.adj_list.items():
			print(f"{key} -> {val}")
		print()

	def in_degree_of_vertex(self, vertex):
		inDeg = 0
		for key, val in self.adj_list.items():
			if key != vertex:
				for i in val:
					if i == vertex:
						inDeg += 1
		return inDeg

	def out_degree_of_vertex(self, vertex):
		deg = len(self.adj_list[vertex])
		return deg

	def graph_breath_first_search(self, src):
		visited = set()
		queue = deque([src])
		bfs_order = []

		while queue:
			vertex = queue.popleft()
			if vertex not in visited:
				visited.add(vertex)
				bfs_order.append(vertex)

			for neighbor in self.adj_list[vertex]:
				if neighbor not in visited:
					queue.append(neighbor)
		return bfs_order

	def graph_depth_first_search(self, src):
		pass

	def detect_cycles(self):
		pass

def edges_to_adj_list_undirected(edges):
	graph = {}

	for edge in edges:
		u, v = edge
		if u not in graph:
			graph[u] = []
		if v not in graph:
			graph[v] = []
		graph[u].append(v)
		graph[v].append(u)
	return graph

def edge_to_adj_list_directed(edges):
	graph = defaultdict(list)

	for edge in edges:
		u, v = edge
		graph[u].append(v)
	return graph


# nodes = ["A", "B", "C", "D", "E"]
# graph = Graph(nodes, is_directed=True)
# graph.print_list()

# all_edges = [("A", "B"), ("E", "A"), ("B", "E"), ("D", "E"), ("D", "C"), ("B", "D"), ("C", "B")]
# for u, v in all_edges:
# 	graph.add_edge(u, v)

# graph.print_list()

# print(f"Degree of E: {graph.out_degree_of_vertex("E")}")
# print(f"Degree of B: {graph.in_degree_of_vertex("B")}")



graph2 = Graph(is_directed=False)
graph2.print_list()

list_of_edges = [
	("A", "B"), ("A", "D"), ("B", "C"),
	("D", "F"), ("D", "E"), ("E", "G"),
	("E", "F"), ("F", "H"), ("G", "H")
]
for src, des in list_of_edges:
	graph2.add_edge(src, des)

graph2.print_list()
print(graph2.graph_breath_first_search("A"))