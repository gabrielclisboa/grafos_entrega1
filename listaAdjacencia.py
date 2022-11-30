from Aresta import *

class ListaAdjacencia():
    def __init__(self,tipoGrafo):
        self.listaAdjacencia = {}
        self.ponderacaoVertice = {}
        self.ponderacaoAresta = {}
        self.rotulacaoAresta = {}
        self.tipoGrafo = tipoGrafo

    def addVertice(self,vertice):
        self.listaAdjacencia[vertice] = []

    def addAresta(self,vertice,verticeAdjacente):
        if(self.verificaExistenciaVertice(vertice) and self.verificaExistenciaVertice(verticeAdjacente)):
            self.listaAdjacencia[vertice].append(verticeAdjacente)
            if(self.tipoGrafo == 0):
                self.listaAdjacencia[verticeAdjacente].append(vertice)


    def removeAresta(self,vertice,verticeAdjacente):
        if(vertice in self.ponderacaoAresta):
            self.ponderacaoAresta[vertice].remove(verticeAdjacente)
        if(vertice in self.rotulacaoAresta):
            self.rotulacaoAresta[vertice].remove(verticeAdjacente)
            
        self.listaAdjacencia[vertice].remove(verticeAdjacente)
        if(self.tipoGrafo == 0):
            self.listaAdjacencia[verticeAdjacente].remove(vertice)

    def addPonderacaoAresta(self,aresta:Aresta,valor):
       self.ponderacaoAresta[aresta] = valor

    def addPonderacaoVertice(self,vertice,valor):
       self.ponderacaoVertice[vertice] = valor

    def addRotulacaoAresta(self,aresta:Aresta,rotulo):
       self.rotulacaoAresta[aresta] = rotulo

    def verificaExistenciaAresta(self,vertice,verticeAdjacente):
        return True if verticeAdjacente in self.listaAdjacencia[vertice] else False
    
    def verificaExistenciaVertice(self,vertice):
        return True if vertice in self.listaAdjacencia else False
    
    def verificaAdjacenciaVertices(self,vertice, verticeAdjacete):
        return True if vertice in self.listaAdjacencia[verticeAdjacete] else False
    
    def verificaAdjacenciaArestas(self,aresta:Aresta,arestaAdjacente:Aresta):
        if (aresta != arestaAdjacente): 
            if (self.tipoGrafo == 0):
                return aresta.vertice1 == arestaAdjacente.vertice1 or aresta.vertice2 == arestaAdjacente.vertice2 or aresta.vertice1 == arestaAdjacente.vertice2 or arestaAdjacente.vertice1 == aresta.vertice2
            else: 
                return aresta.vertice1 == arestaAdjacente.vertice1
        else: 
            return False
        
    def quantidadeAresta(self):
        length = 0
        for key,value in self.listaAdjacencia.items():
            length += len(value)
        return length if self.tipoGrafo != 0 else int(length/2)
    
    def quantidadeVertices(self):
        return len(self.listaAdjacencia.keys())

    def verificaGrafoCompleto(self):
       valid = True
       for key, value in self.listaAdjacencia.items():
        for key1, value1 in self.listaAdjacencia.items():
            if(key != key1):
                if(value1.count(key) == 0):
                    valid = False
       return valid
    
    def verificaGrafoVazio(self):
       valid = True
       for key, value in self.listaAdjacencia.items():
        if(len(value) > 0):
            valid = False
       return valid
    

    def printListaAdjacencia(self):
       for key, value in self.listaAdjacencia.items():
          print(key+" "+value)
        
    def printVertices(self):
       for key, value in self.listaAdjacencia.items():
          ponderacao = self.printPonderacaoVertice(key)
          print(f'{key} - Ponderação: {ponderacao}')

    def printArestas(self):
        listaVerticesAcessados = []
        for key,value in self.listaAdjacencia.items():
            listaVerticesAcessados.append(key)
            for vertice in value:
                 if(vertice not in listaVerticesAcessados):
                    aresta = Aresta(key,vertice)
                    rotulo = self.printRotulacaoAresta(aresta)
                    ponderacao = self.printPonderacaoAresta(aresta)
                    print(f'({key},{vertice}) - Ponderação: {ponderacao} | Rotulação: {rotulo}')
                    
    def printPonderacaoAresta(self,aresta:Aresta):
        return (self.ponderacaoAresta[aresta]) if aresta in self.ponderacaoAresta else ""

    def printRotulacaoAresta(self,aresta:Aresta):
        return (self.rotulacaoAresta[aresta]) if aresta in self.rotulacaoAresta else ""

    def printPonderacaoVertice(self,vertice):
       return (self.ponderacaoVertice[vertice]) if vertice in self.ponderacaoVertice else ""
