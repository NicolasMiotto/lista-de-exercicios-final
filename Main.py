from Apartamento import Apartamento
from Torre import Torre


b1 = Torre()
b1.cadastrar()
b1.imprime()

b2 = Torre()
b2.cadastrar()
b2.imprime()

ap1 = Apartamento()
ap1.cadastra(b1)
ap1.imprime()

ap2 = Apartamento()
ap2.cadastra(b2)
ap2.imprime()