'''
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}
'''


class Graph:

    graph_dict = {}

    def add_edge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
            return

        self.graph_dict[node].append(neighbour)

    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(",node,", ",neighbour,")")

    def find_path(self, start, end, path=[]):
        path.append(start)

        if start == end:
            return path

        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path:
                    return new_path
                return None


g= Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'A')
g.add_edge('C', 'A')
g.add_edge('C', 'B')
g.add_edge('C', 'D')
g.add_edge('D', 'C')
g.show_edges()
print(g.graph_dict)
print(g.find_path('D', 'A'))
