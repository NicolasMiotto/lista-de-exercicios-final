from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adiciona(self, valor):
        no = No(valor)
        if self.tamanho == 0:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1

    def remove(self):
        if self.tamanho == 0:
            print("vazia")
        elif self.tamanho == 1:
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
        else:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1

    def imprime(self):
            texto = ""
            if self.tamanho == 0:
                texto = "Vazia"
            else:
                aux = self.inicio
                while (aux):
                    texto = texto + str(aux.dado) + " ---- "
                    aux = aux.proximo
            print(texto)