import cv2
import numpy as np
from matplotlib import pyplot as plt

class Imagem:
    def __init__(self, caminho_imagem):
        # Carrega a imagem em tons de cinza
        self.img_original = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
        if self.img_original is None:
            raise ValueError("Erro ao carregar a imagem.")
        self.img_normalizada = self.img_original / 255.0

    def mostrar_imagem(self, imagem, titulo="Imagem"):
        plt.imshow(imagem, cmap='gray')
        plt.title(titulo)
        plt.axis('off')
        plt.show()

    def calcular_histograma(self):
        # Histograma da imagem normalizada
        hist, bins = np.histogram(self.img_original.flatten(), bins=256, range=[0, 256])
        return hist

    def equalizar_histograma(self):
        # Passo 1: Montagem do histograma
        hist = self.calcular_histograma()
        n_pixels = self.img_original.size
        
        # Passo 2: Cálculo da soma normalizada do histograma (CDF)
        cdf = hist.cumsum()
        cdf_normalizado = cdf / n_pixels

        # Passo 3: Criação da Look-Up Table (LUT)
        lut = np.floor(255 * cdf_normalizado).astype('uint8')

        # Passo 4: Transformação da imagem de entrada na imagem de saída
        img_equalizada = lut[self.img_original]

        return img_equalizada, hist, cdf_normalizado
 