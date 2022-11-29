from Aresta import *
import igraph as ig

#https://www.programiz.com/dsa/graph-adjacency-matrix
#https://stackoverflow.com/questions/30451252/print-5-items-in-a-row-on-separate-lines-for-a-list
class MatrizAdjacencia():

    def __init__(self, size,rotulos):
        self.rotulacaoVertice = {}
        self.ponderacaoVertice = {}

        self.rotulacaoAresta = {}
        self.auxVerticeIndice = {}
        self.adjMatrix = []
        for i in range(size):
            self.addRotulacaoVertice(rotulos[i],i)
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Aresta entre os vértices %d e %d , já existe" % (v1, v2))
        self.adjMatrix[self.rotulacaoVertice[v1]][self.rotulacaoVertice[v2]] = 1
        self.adjMatrix[self.rotulacaoVertice[v2]][self.rotulacaoVertice[v1]] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if(v1 in self.ponderacaoAresta):
            self.ponderacaoAresta[v1].remove(v2)
        if(v1 in self.rotulacaoAresta):
            self.rotulacaoAresta[v1].remove(v2)

        if self.adjMatrix[self.rotulacaoVertice[v1]][self.rotulacaoVertice[v2]] == 0:
            print("Nenhuma aresta entre %d e %d" % (v1, v2))
            return
        self.adjMatrix[self.rotulacaoVertice[v1]][self.rotulacaoVertice[v2]] = 0
        self.adjMatrix[self.rotulacaoVertice[v2]][self.rotulacaoVertice[v1]] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for i in self.adjMatrix:
            print('\t'.join(map(str, i)))

    def addPonderacaoAresta(self,v1,v2,valor):
       self.adjMatrix[self.rotulacaoVertice[v1]][self.rotulacaoVertice[v2]] = valor
       self.adjMatrix[self.rotulacaoVertice[v2]][self.rotulacaoVertice[v1]] = valor

    def addRotulacaoAresta(self,aresta:Aresta,rotulo):
       self.rotulacaoAresta[aresta] = rotulo

    def addPonderacaoVertice(self,vertice,valor):
       self.ponderacaoVertice[vertice] = valor

    def addRotulacaoVertice(self,vertice,indice):
       self.rotulacaoVertice[vertice] = indice
       self.auxVerticeIndice[indice] = vertice

    def verificaExistenciaAresta(self,v1,v2):
        return True if self.adjMatrix[self.rotulacaoVertice[v1]][self.rotulacaoVertice[v2]] != 0 else False

    def printArestas(self):
        listaVerticesVisitados = []
        for i in range(len(self.adjMatrix)):
            for j in range(len(self.adjMatrix)):
                if(self.adjMatrix[i][j] != 0 and j not in listaVerticesVisitados):
                    v1 = self.auxVerticeIndice[i]
                    v2 = self.auxVerticeIndice[j]
                    ponderacao = self.adjMatrix[i][j]
                    rotulo = self.printRotulacaoAresta(Aresta(v1,v2))
                    print(f'({v1},{v2}) - Ponderação: {ponderacao} | Rotulação: {rotulo}')
            listaVerticesVisitados.append(i)
                    

    def printRotulacaoAresta(self,aresta:Aresta):
        return (self.rotulacaoAresta[aresta]) if aresta in self.rotulacaoAresta else ""

    def importarArquivo(self):
        grafo = ig.Graph()
        grafo = ig.load("entrada.gml")
        self.adjMatrix =grafo.get_adjacency()


            

            
g = MatrizAdjacencia(5,["a","b","c","d","e"])
# g.add_edge("a", "b")
# g.add_edge("b", "c")
# g.add_edge("c", "d")
# g.add_edge("d", "a")
# g.add_edge("a", "c")

# # g.addPonderacaoAresta("a","b",12)
# # g.addRotulacaoAresta(Aresta("a","b"),"carlos")

# # g.printArestas()

# g.print_matrix()


g.importarArquivo()

g.printArestas()

g.print_matrix()
