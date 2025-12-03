import networkx as nx


class PadGraph(nx.Graph):
    def __init__(self, start=None):
        super().__init__(start)
    # here are some of the public methods to implement
    # add_edge, .edges, remove edge are already inbuilt
    def vertices(self):
        return self.nodes()
    def add_vertex(self,n):
        return self.add_node(n)
    def get_vertex_value(self, v):
        return self.nodes[v]
    def set_vertex_value(self, v, x):
        self._node[v] = x
    def remove_vertex(self,v):
        self.remove_node(v)
    def neighbors(self, n):
        return list(self._adj[n])
    

with open("2024/day21/day21.txt") as File:

    num_pad =[["7","8","9"],
              ["4","5","6"],
              ["1","2","3"],
              ["-","0","A"]]
    
    key_pad =[["-","^","A"],
              ["<","v",">"]]
    g = PadGraph()
    for x in num_pad:
        for y in x:
            g.add_vertex(y)


    print(g.vertices())
    list1,list2 = [],[]
    for row in File.read().split():
        print(row)