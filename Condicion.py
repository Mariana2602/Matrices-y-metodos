# Alejandro Lopez 30914440
# Yexibel Aguero 31268552
# Mariana Lopez 30913839
import matplotlib.pyplot as plt
import random

class MatrizCondicion:
    def __init__(self, matriz):
        self.matriz = matriz
        self.filas = len(matriz)
        self.columnas = len(matriz[0])

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

    def norma(self, matriz):
        return max(sum(abs(j) for j in i) for i in matriz)

    def calcular_condicion(self):
        inversa = self.inversa()
        if inversa is None:
            return None
        normaMatriz = self.norma(self.matriz) 
        normaInversa = self.norma(inversa) 

        return round(normaMatriz * normaInversa, 2)

    def mostrar(self, matriz):
        for i in matriz:
            print(["{:.2f}".format(valor) for valor in i])

tam = list(range(2, 11))
condiciones = []

for i in tam:
    matriz = [[random.randint(1, 9) for _ in range(i)] for _ in range(i)]
    matriz_condicion = MatrizCondicion(matriz)
    condicion = matriz_condicion.calcular_condicion()
    if condicion is not None:
        condiciones.append(condicion)
    else:
        condiciones.append(0)

plt.figure(figsize=(8, 5))
plt.plot(tam, condiciones, marker='o', linestyle='-', color='b', label="Número de condición")
plt.xlabel("Tamaño de la Matriz")
plt.ylabel("Número de Condición")
plt.title("Número de Condición en función del Tamaño de la Matriz")
plt.legend()
plt.grid()
plt.show()
