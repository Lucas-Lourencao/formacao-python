import pytest 

# Importanto as funções no módulo externo com as funções
from verificaNumero import verificaMultiplo_5

#Criando uma classe para realização do teste:
class verificaMultiplo:
    #def setup é similar ao def __init__, mas é o modo recomendado de iniciar uma função no pytest;
    def setup(self):
        self.multiplo = int(input('Informe um número natural: '))

    def multiploCinco(self):
        resultado = verificaMultiplo_5(self.multiplo)

        assert resultado == 5


# numNatural = int(input('Informe um número: '))

# print(numNatural)

