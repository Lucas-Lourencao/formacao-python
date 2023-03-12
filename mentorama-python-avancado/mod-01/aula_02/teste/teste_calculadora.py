import pytest

from calculadora import soma, subtracao, multiplicacao, divisao

#Criando uma classe para realização do teste:
class testeCalculadora:
    #def setup é similar ao def __init__, mas é o modo recomendado de iniciar uma função no pytest;
    def setup(self):
        pass

    # Teste da função soma:
    def test_soma(self):
        resultado = soma(2, 3)
        #resultado_2 = soma(5, 8)

        assert resultado == 5

        # assert inserido com erro proposital
        #assert resultado_2 <= 13

    # Teste da função subtração:
    def test_subtracao(self):
        resultado = subtracao(3, 2)

        assert resultado == 1


    # Teste da função multiplicação:
    def test_multiplicacao(self):
        resultado = multiplicacao(2, 3)

        assert resultado == 6

    # Teste da função divisão:
    def test_divisao(self):
        resultado = divisao(3, 3)

        assert resultado == 1