class Aresta():
    vertice1=""
    vertice2=""
    def __init__(self, vertice1, vertice2):
        self.vertice = vertice1
        self.verticeAdjacente = vertice2

    def __hash__(self):
        return hash((self.vertice1, self.vertice2))