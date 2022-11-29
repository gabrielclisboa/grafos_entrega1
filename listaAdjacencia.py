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
            self.listaAdjacencia[vertice] = self.listaAdjacencia[vertice].append(verticeAdjacente)
            if(self.tipoGrafo == 0):
                self.listaAdjacencia[verticeAdjacente] = self.listaAdjacencia[verticeAdjacente].append(vertice)


    def removeAresta(self,vertice,verticeAdjacente):
        self.listaAdjacencia[vertice] = self.listaAdjacencia[vertice].remove(verticeAdjacente)
        if(self.tipoGrafo == 0):
            self.listaAdjacencia[verticeAdjacente] = self.listaAdjacencia[verticeAdjacente].remove(vertice)

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
                return aresta.vertice1 == arestaAdjacente.vertice2 or aresta.vertice1 == arestaAdjacente.vertice1 or aresta.vertice2 == arestaAdjacente.vertice2
            else: 
                return aresta.vertice1 == arestaAdjacente.vertice1
        else: 
            return False
        
    def quantidadeAresta(self):
        length = 0
        for vertice in self.listaAdjacencia:
            length += len(vertice.values())
        return length
    
    def quantidadeVertices(self):
        return len(self.listaAdjacencia.keys())

    def verificaGrafoCompleto(self):
       valid = True
       for key, value in self.listaAdjacencia.items():
        for key1, value1 in self.listaAdjacencia.items():
         if(key != key1):
          if(value1.count(key) > 0):
           valid = False
        return valid
    
    def verificaGrafoVazio(self):
       return False if len(self.listaAdjacencia.values()) > 0 else True
    

    def printListaAdjacencia(self):
       for key, value in self.listaAdjacencia.items():
          print(key+" "+value)
        
    def printVertices(self):
       for key, value in self.listaAdjacencia.items():
          print(key)


    def printPonderacaoVertice(self,vertice):
       return print("- Ponderação: "+ self.ponderacaoVertice[vertice])

    def printArestas(self):
        listaVerticesAcessados = []
        for key,value in self.listaAdjacencia.items():
            print(key)
            print(value)
            for vertice in list(value):
                if(key not in listaVerticesAcessados):
                    print("("+ key+","+vertice+")"+self.printPonderacaoAresta(Aresta(key,vertice))+self.printRotulacaoAresta(Aresta(key,vertice)))
            listaVerticesAcessados.append(key)

    def printPonderacaoAresta(self,aresta:Aresta):
        return (' - Ponderação: '+ self.ponderacaoAresta[aresta])

    def printRotulacaoAresta(self,aresta:Aresta):
        return (' - Rotulação: '+ self.rotulacaoAresta[aresta])
    


g = ListaAdjacencia(0)

g.addVertice("a")
g.addVertice("b")
g.addVertice("c")
g.addVertice("d")

g.addAresta("a","b")
#g.printVertices()
g.printArestas()