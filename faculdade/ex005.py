class Fila():
    def __init__(self):
        self.data = []
        
    def inserir(self, x):
        self.data.append(x)
        
    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
    
    def empty(self):
        return not len(self.data) > 0    
    
fila_prioritaria = Fila()
fila_normal = Fila()

while True:
    idade = int(input("Digite a idade: "))
    if idade == 0:
        break
    elif idade >= 60:
        fila_prioritaria.inserir(idade)
    else:
        fila_normal.inserir(idade)

print("\n--- Atendimento iniciado! ---")
cont_prioridade = 0

while not fila_prioritaria.empty() or not fila_normal.empty():   
    if cont_prioridade < 2 and not fila_prioritaria.empty():
        print(f"Atendendo Prioritário: {fila_prioritaria.remover()}")
        cont_prioridade += 1
    elif not fila_normal.empty():
        print(f"Atendendo Normal: {fila_normal.remover()}")
        cont_prioridade = 0
    else:
        print(f"Atendendo Prioritário (extra): {fila_prioritaria.remover()}")