# Refatoração
# Renomear todas as ocorrências - F2

class Calculadora:
    pass


calc1 = Calculadora()
calc2 = Calculadora()
calc3 = Calculadora()

print(calc1)
# Extrair uma função (CTRL-SHIFT-P -> Extract Method - Atalho: em)


def adicao():
    resultado = 20 + 50


adicao()
# Extrair uma variável (CTRL-SHIF-P Extratct Variable - Atanho: ev)
tamanho = (60/2) + 50
