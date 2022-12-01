from Aresta import *

class ListaAdjacencia():
    def __init__(self,tipoGrafo):
        self.listaAdjacencia = {}
        self.ponderacaoVertice = {}
        self.ponderacaoAresta = {}
        self.rotulacaoAresta = {}
        self.tipoGrafo = tipoGrafo

    def addVertice(self,v):
        self.listaAdjacencia[v] = []

    def addAresta(self,v1,v2):
        if(self.verificaExistenciaVertice(v1) and self.verificaExistenciaVertice(v2)):
            self.listaAdjacencia[v1].append(v2)
            if(self.tipoGrafo == 0):
                self.listaAdjacencia[v2].append(v1)

    def removeAresta(self,v1,v2):
        if(self.verificaExistenciaAresta(Aresta(v1,v2))):
            if(v1 in self.ponderacaoAresta):
                self.ponderacaoAresta[v1].remove(v2)
            if(v1 in self.rotulacaoAresta):
                self.rotulacaoAresta[v1].remove(v2)
            
            self.listaAdjacencia[v1].remove(v2)
            if(self.tipoGrafo == 0):
                self.listaAdjacencia[v2].remove(v1)

    def addPonderacaoAresta(self,v1,v2,valor):
       if(self.verificaExistenciaAresta(Aresta(v1,v2))):
            aresta = Aresta(v1,v2)
            self.ponderacaoAresta[aresta] = valor

    def addPonderacaoVertice(self,v,valor):
       if(self.verificaExistenciaVertice(v)):
            self.ponderacaoVertice[v] = valor

    def addRotulacaoAresta(self,v1,v2,rotulo):
       if(self.verificaExistenciaAresta(Aresta(v1,v2))):
            aresta = Aresta(v1,v2)
            self.rotulacaoAresta[aresta] = rotulo

    def verificaExistenciaAresta(self,v1,v2):
        return True if v2 in self.listaAdjacencia[v1] else False
    
    def verificaExistenciaVertice(self,v):
        return True if v in self.listaAdjacencia else False
    
    def verificaAdjacenciaVertices(self,v1, v2):
        return True if v1 in self.listaAdjacencia[v2] else False
    
    def verificaAdjacenciaArestas(self,aresta:Aresta,arestaAdjacente:Aresta):
        if (aresta != arestaAdjacente and self.verificaExistenciaAresta(Aresta(aresta)) and self.verificaExistenciaAresta(Aresta(arestaAdjacente))): 
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
    
    def importarArquivo(self):
        self.printListaAdjacencia()
    
    def exportandoArquivo(self):
        self.printListaAdjacencia()
