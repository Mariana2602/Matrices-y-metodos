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
        vector = [random.uniform(0, 1) for i in range(n)]

        autovalor_anterior = 0
        autovalor_convergencia = []
        autovector_convergencia = []

        for i in range(self.iteraciones):
            nuevo_vector = self.matriz_vector(self.matriz, vector)
            norma = self.norma(nuevo_vector)
            vector = [x / norma for x in nuevo_vector]
            autovalor = sum(vector[i] * nuevo_vector[i] for i in range(n))
            autovalor_convergencia.append(autovalor)
            autovector_convergencia.append(list(vector))
            if abs(autovalor - autovalor_anterior) < self.tolerancia:
                break

            autovalor_anterior = autovalor

        return autovalor_convergencia, autovector_convergencia

n = 2 
matriz = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]
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
    plt.plot(range(1, len(autovectores) + 1), autovectores, marker='o', linestyle='-', label=f'Componente {i+1}')
plt.xlabel("Iteraciones")
plt.ylabel("Valor de la Componente")
plt.title("Convergencia de las Componentes del Autovector")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
