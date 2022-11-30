from Aresta import *
import pandas as pd
import numpy as np
import igraph as ig

#https://www.programiz.com/dsa/graph-adjacency-matrix
#https://stackoverflow.com/questions/30451252/print-5-items-in-a-row-on-separate-lines-for-a-list
class MatrizAdjacencia():

    def __init__(self,rotulos,size):
        self.ponderacaoVertice = {}
        self.rotulacaoAresta = {}
        self.adjMatrix = []

        matrix = np.reshape(([0 for i in range(size*size)]), (size, size))
        self.adjMatrix = pd.DataFrame(matrix, columns=rotulos, index=rotulos)
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Aresta entre os vértices %d e %d , já existe" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("Nenhuma aresta entre %d e %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        print(self.adjMatrix)

    def addPonderacaoAresta(self,v1,v2,valor):
       self.adjMatrix[v1][v2] = valor
       self.adjMatrix[v2][v1] = valor

    def addRotulacaoAresta(self,v1,v2,rotulo):
       aresta = Aresta(v1,v2)
       self.rotulacaoAresta[aresta] = rotulo

    def addPonderacaoVertice(self,v,valor):
       self.ponderacaoVertice[v] = valor

    def printArestas(self):
        listaVerticesVisitados = []
        df = self.adjMatrix
        df.reset_index(drop=True)
        for v1 in self.adjMatrix.keys():
            for v2 in self.adjMatrix.keys():
                if(df[v1][v2] != 0 and v2 not in listaVerticesVisitados):
                    ponderacao = df[v1][v2]
                    rotulo = self.printRotulacaoAresta(v1,v2)
                    print(f'({v1},{v2}) - Ponderação: {ponderacao} | Rotulação: {rotulo}')
            listaVerticesVisitados.append(v1)

    def printRotulacaoAresta(self,v1,v2):
        aresta = Aresta(v1,v2)
        return (self.rotulacaoAresta[aresta]) if aresta in self.rotulacaoAresta else ""

    def verificaExistenciaVertice(self,v):
        return True if v in self.ponderacaoVertice else False

    def verificaExistenciaAresta(self,v1,v2):
        return True if self.adjMatrix[v1][v2] != 0 else False

    def verificaAdjacenciaVertices(self,v1, v2):
        return True if self.adjMatrix[v1][v2] != 0 else False

    def verificaAdjacenciaArestas(self,a1:Aresta,a2:Aresta):
        if ((a1 != a2) and self.verificaExistenciaAresta(a1.vertice1,a1.vertice2) and self.verificaExistenciaAresta(a2.vertice1,a2.vertice2)): 
            if (self.tipoGrafo == 0):
                return a1.vertice1 == a2.vertice1 or a1.vertice2 == a2.vertice2 or a1.vertice1 == a2.vertice2 or a2.vertice1 == a1.vertice2
            else: 
                return a1.vertice1 == a2.vertice1
        else: 
            return False

    def quantidadeAresta(self):
        length = 0
        for v1 in self.adjMatrix.keys():
            for v2 in self.adjMatrix.keys():
                if(self.adjMatrix[v1][v2] != 0):
                    length += 1
        return int(length/2)
    
    def quantidadeVertices(self):
        return len(self.adjMatrix)


    def verificaGrafoCompleto(self):
       valid = True
       for v1 in self.adjMatrix.keys():
        for v2 in self.adjMatrix.keys():
            if(self.adjMatrix[v1][v2]==0 and v1 != v2):
                valid = False    
       return valid
    
    def verificaGrafoVazio(self):
       valid = True
       for v1 in self.adjMatrix.keys():
        for v2 in self.adjMatrix.keys():
            if(self.adjMatrix[v1][v2] !=0):
                valid = False    
       return valid 
    
    def importarArquivo(self):
        grafo = ig.Graph()
        grafo = ig.load("entrada.gml")
        self.adjMatrix = pd.DataFrame(grafo.get_adjacency(), columns=["a","b","c","d","e","f"], index=["a","b","c","d","e","f"])
        self.print_matrix()
        
        
    

            
kek = ["a","b","c"]
g = MatrizAdjacencia(kek,3)
g.importarArquivo()

# g.add_edge("a","b")
# g.add_edge("b","c")
# g.add_edge("c","a")


# g.addPonderacaoAresta("a","b",12)
# g.addPonderacaoAresta("a","b",1)
# g.addRotulacaoAresta("a","b","carlos")
# g.print_matrix()
# g.printArestas()
