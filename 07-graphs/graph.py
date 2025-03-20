
class Vertex:
    def __init__(self, key):
        self.key = key 
        self.data = None 
        self.edges = [] 

    def display(self):
        print(self.key, " ", self.data, end=": [ ")
        for edge in self.edges:
            print(edge.connection.key, end=" ")
        print("]")


class Edge:
    def __init__(self, vertex):
        self.connection = vertex
        self.weight = 1


class Graph:
    def __init__(self):
        self.vertices = {} 
        self.directed = False

    def display(self): 
        for key in self.vertices:
            self.vertices[key].display()

    def add(self, key):
        if key in self.vertices:
            return None
        else:
            new_vertex = Vertex(key)
            self.vertices[key] = new_vertex
            return new_vertex

    def connect(self, key_a, key_b):
        if key_a not in self.vertices or key_b not in self.vertices:
            return False, "Key not found"
        else:
            vertex_a = self.vertices[key_a]
            vertex_b = self.vertices[key_b]
            edge = Edge(vertex_b)
            vertex_a.edges.append(edge)
            if not self.directed:
                edge = Edge(vertex_a)
                vertex_b.edges.append(edge) 
            return True, "Vertices connected"


if __name__ == "__main__":
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data = ["S", "M", "N", "F", "AD", "P", "L", "AN", "T", "Z"]
    edges = [(1, 2), (1, 3), (2, 4), (2, 6), (2, 7), (3, 4), (3, 5),
            (5, 7), (6, 7), (6, 8), (7, 10), (8, 9), (9, 10)]
    graph = Graph()
    for key in keys:
        v = graph.add(key)
        if v is not None:
            v.data = data[keys.index(key)]
    for pair in edges:
        graph.connect(pair[0], pair[1])
    graph.display()