from calculadoraAssert import soma

# OBSERVAÇÃO:
# Lembrar de comentar os códigos para executar. Executar um bloco de código
# por vez!

# Utilizando ASSERT;
# AssertionError-Exemplo-01:
print(soma('15', 5))  # output -> AssertionError: x precisa ser Int ou Float;

# AssertionError-Exemplo-02:
print(soma(15, '5'))  # output -> AssertionError: y precisa ser Int ou Float;

# AssertionError-Exemplo-03: Utilizando o Try/Except:
try:
    print(soma(15, '5'))
except AssertionError as e:
    # Além da mensagem personalizada mostra o log;
    print(f'Conta inválida - {e}')
