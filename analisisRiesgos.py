# Alejandro Lopez 30914440
# Yexibel Aguero 31268552
# Mariana Lopez 30913839
import random
from Potencia import Potencia
from PotenciaInverso import PotenciaInversa
from Condicion import MatrizCondicion

class MatrizCovarianza:
    def __init__(self, tam):
        self.tam = tam
        self.matriz = self.generar_matriz()

    def generar_matriz(self):
        matriz = [[random.uniform(0.5, 2.0) for _ in range(self.tam)] for _ in range(self.tam)]
        for i in range(self.tam):
            for j in range(i, self.tam):
                matriz[j][i] = matriz[i][j]
        return matriz

if __name__ == "__main__":
    matriz_covarianza = MatrizCovarianza(3)
    condicion = MatrizCondicion(matriz_covarianza.matriz).calcular_condicion()
    print(f"Número de Condición: {condicion}")
    potencia = Potencia(matriz_covarianza.matriz)
    autovalor_dominante, autovector_dominante = potencia.potencia()
    print(f"Autovalor Dominante: {autovalor_dominante[-1]}")
    potencia_inversa = PotenciaInversa(matriz_covarianza.matriz)
    autovalor_min, autovector_min = potencia_inversa.potencia()
    print(f"Autovalor Mínimo: {autovalor_min[-1]}")