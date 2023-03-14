import pytest 

# Importanto as funções no módulo externo com as funções
from verificaNumero import verificaMultiplo_5, verificaMultiplo_7, verificaM5_M7

#Criando uma classe para realização do teste:
class verificaMultiplo:
    #def setup é similar ao def __init__, mas é o modo recomendado de iniciar uma função no pytest;
    def setup(self):
        pass

    def multiploCinco(self):
        teste_resultado = verificaMultiplo_5()

        assert teste_resultado == ("fizz", 'O número informado não é múltiplo de 5!', 'Você precisa informar um número natural, ou seja, inteiro e positivo!')

    def multiploSete(self):
        teste_resultado = verificaMultiplo_7()

        assert teste_resultado == ("buzz", 'O número informado não é múltiplo de 7!', 'Você precisa informar um número natural, ou seja, inteiro e positivo!')
    
    def multiploCincoSete(self):
        teste_resultado = verificaM5_M7()

        assert teste_resultado == ("fizzbuzz", 'miss', 'Você precisa informar um número natural, ou seja, inteiro e positivo!')


# numNatural = int(input('Informe um número: '))

# print(numNatural)

