class Apartamento:
    def __init__(self):
        self.id = int()
        self.numero = str()
        self.torre = None
        self.vaga = int()
        self.proximo = None

    def cadastra(self, valor):
        self.id = int(input("Entre com o id do apartamento: "))
        self.numero = str(input("Entre com o número do apartamento: "))
        self.torre = valor

    def imprime(self):
        print("Id do Apartamento:" ,self.id)
        print( "Número: " , self.numero) 
        print("Torre: ", self.torre.nome)