from PIL import Image
import numpy as np

class Imagem:
    def __init__(self, caminho_imagem):
        self.imagem = Image.open(caminho_imagem).convert("L")  # Converte para escala de cinza
        self.matriz = np.array(self.imagem)

    def transformar_negativo(self):
        L = 256
        negativa = L - 1 - self.matriz
        return Image.fromarray(negativa.astype(np.uint8))
