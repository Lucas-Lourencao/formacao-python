# Módulo com funções que serão importadas

# Função que verifica se o número informado é múltiplo de 5 e satisfaz as demais condições:
def verificaMultiplo_5():
    try:
        numeroNatural = int(input('Informe um número natural: '))
        if numeroNatural % 5 == 0 and numeroNatural >= 0:
            resultado = print('fizz')
        else:
            resultado = print('O número informado não é múltiplo de 5!')
    except:
        resultado = 'Você precisa informar um número natural, ou seja, inteiro e positivo!'

    return resultado

# Função que verifica se o número informado é múltiplo de 7 e satisfaz as demais condições:


def verificaMultiplo_7():
    try:
        numeroNatural = int(input('Informe um número natural: '))
        if numeroNatural % 7 == 0 and numeroNatural >= 0:
            resultado = print('buzz')
        else:
            resultado = print('O número informado não é múltiplo de 7!')
    except:
        resultado = 'Você precisa informar um número natural, ou seja, inteiro e positivo!'

    return resultado

# Função que verifica se o número informado é múltiplo de 5, 7 e satisfaz as demais condições:


def verificaM5_M7():
    try:
        numeroNatural = int(input('Informe um número natural: '))
        if numeroNatural % 5 == 0 and numeroNatural % 7 == 0 and numeroNatural >= 0:
            resultado = print('fizzbuzz')
        else:
            resultado = print('miss')
    except:
        resultado = 'Você precisa informar um número natural, ou seja, inteiro e positivo!'

    return resultado


# def verificaMultiplo_7(numeroNatural):
#     if numeroNatural % 7 == 0:
#         return 'fizz'

# def verificaMultiplo_5e7(numeroNatural):
#     if numeroNatural % 5 == 0 & numeroNatural % 7 == 0:
#         return 'fizzbuzz'
