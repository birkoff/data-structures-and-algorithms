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

    def depth_first_search(self, start, end, path=[]):
        path.append(start)

        if start == end:
            return path

        for node in self.graph_dict[start]:  # Iterate the graph_dict values (neighbours)
            if node not in path:
                new_path = self.depth_first_search(node, end, path)  # change to new key on graph_dict
                if new_path:
                    return new_path
                return None

    def breath_first_search(self, item):
        visited = {}

        for i in self.graph_dict:
            visited[i] = False

        queue = [item]
        visited[item] = True

        while len(queue) > 0:
            item = queue.pop(0)
            for node in self.graph_dict[item]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
                    print(item, end=" ")




if __name__ == '__main__':
    g = Graph()
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
    print(g.depth_first_search('D', 'A'))
    g.breath_first_search('D')
