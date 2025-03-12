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

    def matriz_vector(self, matriz, vector):
        return [sum(matriz[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matriz))]

    def norma(self, vector):
        return sum(i**2 for i in vector) ** 0.5
    
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

    def potencia(self):
        n = len(self.matriz)
        vector = [random.uniform(0, 1) for i in range(n)]
        matriz_inversa = self.inversa()
        if matriz_inversa is None:
            print("La matriz no tiene inversa")
            return None, None

        autovalor_anterior = 0
        autovalor_convergencia = []
        autovector_convergencia = []

        for i in range(self.iteraciones):
            nuevo_vector = self.matriz_vector(matriz_inversa, vector)
            norma = self.norma(nuevo_vector)
            vector = [x / norma for x in nuevo_vector]
            autovalor = sum(vector[i] * nuevo_vector[i] for i in range(n))
            autovalor_convergencia.append(autovalor)
            autovector_convergencia.append(list(vector))
            if abs(autovalor - autovalor_anterior) < self.tolerancia:
                break

            autovalor_anterior = autovalor

        return autovalor_convergencia, autovector_convergencia

matriz = [[random.randint(1, 9) for _ in range(2)] for _ in range(2)]
potencia = PotenciaInversa(matriz)
autovalor_convergencia, autovector_convergencia = potencia.potencia()

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(range(1, len(autovalor_convergencia) + 1), autovalor_convergencia, marker='o', linestyle='-')
plt.xlabel("Iteraciones")
plt.ylabel("Autovalor dominante")
plt.title("Convergencia del Autovalor")
plt.grid()

plt.subplot(1, 2, 2)
for i in range(len(autovector_convergencia[0])): 
    plt.plot(range(1, len(autovector_convergencia) + 1), autovector_convergencia, marker='o', linestyle='-', label=f'Componente {i+1}')
plt.xlabel("Iteraciones")
plt.ylabel("Valor de la Componente")
plt.title("Convergencia del Autovector")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
