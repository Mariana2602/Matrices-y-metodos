# Alejandro Lopez 30914440
# Yexibel Aguero 31268552
# Mariana Lopez 30913839
import random
import matplotlib.pyplot as plt
from Potencia import Potencia
from PotenciaInverso import PotenciaInversa

class Optimizacion:
    def __init__(self, tam):
        self.tam = tam
        self.matriz = self.generar_matriz()

    def generar_matriz(self):
        matriz = [[random.randint(1, 9) for _ in range(self.tam)] for _ in range(self.tam)]
        for i in range(self.tam):
            for j in range(i, self.tam):
                matriz[j][i] = matriz[i][j]
        return matriz
    
    def graficar(self, valores_dominante, valores_inverso):
        plt.plot(range(1, len(valores_dominante) + 1), valores_dominante, marker='o', linestyle='-', label='Autovalor Dominante')
        plt.plot(range(1, len(valores_inverso) + 1), valores_inverso, marker='s', linestyle='--', label='Autovalor Mínimo')
        plt.xlabel('Iteraciones')
        plt.ylabel('Autovalor')
        plt.title('Convergencia del Método de Potencia')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    analisis = Optimizacion(4)
    potencia = Potencia(analisis.matriz)
    potencia_inverso = PotenciaInversa(analisis.matriz)
    for fila in analisis.matriz:
        print([round(val, 2) for val in fila])
    
    autovalor_max, autovector_max, valores_max = potencia.potencia()
    autovalor_min, autovector_min, valores_min = potencia_inverso.potencia()
    
    print("\nAutovalor Dominante:", round(autovalor_max, 4))
    print("Autovector Dominante:", [round(v, 4) for v in autovector_max])
    print("\nAutovalor Mínimo:", round(autovalor_min, 4))
    print("Autovector Mínimo:", [round(v, 4) for v in autovector_min])
    
    print("\nNúmero de Condición:", round((autovalor_max / autovalor_min), 4))
    
    analisis.graficar(valores_max, valores_min)