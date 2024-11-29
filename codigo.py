import random

# Entrada do número de dados e lados
dados = int(input("Quantos dados você quer lançar? "))
lados = int(input("Quantos lados você quer que esses dados tenham? "))

# Paradigma Imperativo
def dados_imperativo(dados, lados):
    resultados = []
    for _ in range(dados):
        resultado = random.randint(1, lados)
        resultados.append(resultado)
    print("Resultados (Imperativo):", resultados)
    
dados_imperativo(dados, lados)

# Paradigma Orientado a Objetos
class Dado:
    def __init__(self, lados):
        self.lados = lados  
    
    def rolar(self):
        return random.randint(1, self.lados)

class SimuladorDados:
    def __init__(self, dados, lados):  
        self.dados = [Dado(lados) for _ in range(dados)]
    
    def simular(self):
        resultados = [dado.rolar() for dado in self.dados]
        print("Resultados (Orientado a Objetos):", resultados) 

simulador = SimuladorDados(dados, lados)
simulador.simular()

# Paradigma Funcional
def rolar_dado(lados):
    return random.randint(1, lados)

def simular_dados_funcional(dados, lados):
    resultados = list(map(lambda _: rolar_dado(lados), range(dados)))
    print("Resultados (Funcional):", resultados)

simular_dados_funcional(dados, lados)
