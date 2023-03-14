from calculadora import soma

# Utilizando Try e Except;
try:
    print(soma('15', 5))
except TypeError as e:  # Veja como exibir uma exceção encontrada;
    print(e, '\nInforme apenas numeros!')
