# Alejandro Lopez 30914440
# Yexibel Aguero 31268552
# Mariana Lopez 30913839
import matplotlib.pyplot as plt
import random

class PotenciaInversa:
    def __init__(self, matriz, tolerancia=1e-6, iteraciones=100):
        self.matriz = matriz
        self.tolerancia = tolerancia
        self.iteraciones = iteraciones
        self.filas = len(matriz)
        self.columnas = len(matriz[0])
        self.matriz_inversa = self.inversa()

    def inversa(self):
        matriz = [i[:] for i in self.matriz]
        identidad = [[1 if i == j else 0 for j in range(self.columnas)] for i in range(self.filas)]

        if self.filas != self.columnas:
            return None

        for i in range(self.filas):
            pivote = matriz[i][i]
            if pivote == 0:
                return None

            for j in range(self.columnas):
                matriz[i][j] /= pivote
                identidad[i][j] /= pivote

            for k in range(self.filas):
                if k != i:
                    factor = matriz[k][i]
                    for j in range(self.columnas):
                        matriz[k][j] -= factor * matriz[i][j]
                        identidad[k][j] -= factor * identidad[i][j]

        return identidad

    def matriz_vector(self, matriz, vector):
        return [sum(matriz[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matriz))]

    def norma(self, vector):
        return sum(i**2 for i in vector) ** 0.5

    def potencia(self):
        n = len(self.matriz)
        vector = [random.uniform(0, 1) for i in range(n)]
        norma_vector = self.norma(vector)
        vector = [x / norma_vector for x in vector]

        autovalores = []

        for _ in range(self.iteraciones):
            nuevo_vector = self.matriz_vector(self.matriz_inversa, vector) 
            lambda_inverso = sum(vector[i] * nuevo_vector[i] for i in range(n))
            autovalor = 1 / lambda_inverso  
            autovalores.append(autovalor)
            
            norma_nuevo = self.norma(nuevo_vector)
            nuevo_vector = [x / norma_nuevo for x in nuevo_vector]
            
            if self.norma([nuevo_vector[i] - vector[i] for i in range(n)]) < self.tolerancia:
                break
            
            vector = nuevo_vector

        return autovalores

matriz = [[random.randint(1, 9) for _ in range(2)] for _ in range(2)]
matriz = [[(matriz[i][j] + matriz[j][i]) // 2 for j in range(2)] for i in range(2)]

potencia = PotenciaInversa(matriz)
autovalores = potencia.potencia()

plt.figure(figsize=(6, 6))
plt.plot(range(1, len(autovalores) + 1), autovalores, marker='o', linestyle='-', color='r')
plt.xlabel("Iteraciones")
plt.ylabel("Autovalor más pequeño")
plt.title("Convergencia del Autovalor más Pequeño")
plt.grid()
plt.show()
