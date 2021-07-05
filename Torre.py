class Torre:
    def __init__(self):
        self.id = int()
        self.nome = str()
        self.endereco = str()

    def cadastrar(self):
        self.id = int(input("Entre com o ID da Torre: "))
        self.nome = str(input("Entre com o Nome da Torre: "))
        self.endereco = str(input("Entre com o Endereço da Torre: "))

    def imprime(self):
        print("Id:" ,self.id)
        print("Nome:" ,self.nome) 
        print ("Endereço:" , self.endereco)