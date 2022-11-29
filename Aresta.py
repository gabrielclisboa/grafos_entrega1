class Aresta():
    def __init__(self, vertice1, vertice2):
        self.vertice1 = vertice1
        self.vertice2 = vertice2

    def __hash__(self):
        return hash((self.vertice1, self.vertice2))
    
    def __eq__(self, other):
        return (self.vertice1, self.vertice2) == (other.vertice1, other.vertice2)