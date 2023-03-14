# Modulo contendo funções a serem exportadas com assertion;
def soma(x, y):
    assert isinstance(x, (int, float)), 'x precisa ser Int ou Float'
    assert isinstance(y, (int, float)), 'y precisa ser Int ou Float'
    return x + y
