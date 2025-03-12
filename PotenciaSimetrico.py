# Alejandro Lopez 30914440
# Yexibel Aguero 31268552
# Mariana Lopez 30913839
import matplotlib.pyplot as plt
import random

class PotenciaSimetrico:
    def __init__(self, matriz, tolerancia=1e-6, iteraciones=100):
        self.matriz = matriz
        self.tolerancia = tolerancia
        self.iteraciones = iteraciones

    def matriz_vector(self, matriz, vector):
        return [sum(matriz[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matriz))]
    
    def norma(self, vector):
        return (sum(i**2 for i in vector)) ** 0.5 

    def potencia(self):
        n = len(self.matriz)
        vector = [random.uniform(0, 1) for _ in range(n)]
        norma_vector = self.norma(vector)
        vector = [v / norma_vector for v in vector] 
        autovalores = []
        autovectores = [] 

        for _ in range(self.iteraciones):
            nuevo_vector = self.matriz_vector(self.matriz, vector)
            autovalor = sum(nuevo_vector[i] / vector[i] for i in range(n)) / n 
            norma_nuevo = self.norma(nuevo_vector)
            nuevo_vector = [v / norma_nuevo for v in nuevo_vector]  
            autovalores.append(autovalor)
            autovectores.append(nuevo_vector[:]) 

            if self.norma([nuevo_vector[i] - vector[i] for i in range(n)]) < self.tolerancia:
                break

            vector = nuevo_vector

        return autovalores, autovectores

n = 2 
matriz = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]
matriz = [[(matriz[i][j] + matriz[j][i]) // 2 for j in range(n)] for i in range(n)] 
potencia = PotenciaSimetrico(matriz)
autovalores, autovectores = potencia.potencia()

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(range(1, len(autovalores) + 1), autovalores, marker='o', linestyle='-', color='b')
plt.xlabel("Iteraciones")
plt.ylabel("Autovalor dominante")
plt.title("Convergencia del Autovalor Dominante")
plt.grid()

plt.subplot(1, 2, 2)
for i in range(n):  
    plt.plot(range(1, len(autovectores) + 1), [vec[i] for vec in autovectores], marker='o', linestyle='-', label=f'Componente {i+1}')
plt.xlabel("Iteraciones")
plt.ylabel("Valor de la Componente")
plt.title("Convergencia de las Componentes del Autovector")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
