class DTONaveSwapi:
    id_nave = None
    nomeFabricante = None
    nome = None
    modelo = None
    tripulacao = None
    passageiros = None
    capacidade_carga = None
    preco = None

    def getIdNave(self):
        return self.id_nave

    def setIdNave(self, idnave):
        self.id_nave = idnave

    def getNomeFabricante(self):
        return self.nomeFabricante
    def setNomeFabricante(self, nomeFabricante):
        self.nomeFabricante = nomeFabricante
    
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome

    def getModelo(self):
        return self.modelo
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getTripulacao(self):
        return self.tripulacao
    def setTripulacao(self, tripulacao):
        self.tripulacao = tripulacao

    def getPassageiros(self):
        return self.passageiros
    def setPassageiros(self, passageiros):
        self.passageiros = passageiros
    
    def getCapacidadeCarga(self):
        return self.capacidade_carga
    def setCapacidadeCarga(self, capacidade_carga):
        self.capacidade_carga = capacidade_carga
    
    def getPreco(self):
        return self.preco
    def setPreco(self, preco):
        self.preco = preco
    
