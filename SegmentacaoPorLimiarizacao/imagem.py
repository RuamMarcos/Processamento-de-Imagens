import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class Imagem:
    def __init__(self, caminho_imagem):
        self.imagem_original = Image.open(caminho_imagem).convert('L')  # Tons de cinza
        self.imagem_pb = np.array(self.imagem_original, dtype=np.uint8)

    def exibir_histograma(self):
        plt.figure(figsize=(10, 4))
        plt.hist(self.imagem_pb.ravel(), bins=256, range=[0, 256], color='gray')
        plt.title('Histograma da Imagem')
        plt.xlabel('Níveis de Cinza')
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.show()

    def encontrar_limiar_metodo_vale(self):
        histograma, _ = np.histogram(self.imagem_pb.ravel(), bins=256, range=(0, 256))
        meio = 128
        limite_direita = np.argmin(histograma[meio:]) + meio
        return limite_direita

    def limiarizar(self, limiar, caminho_saida='segmentada.png'):
        binaria = np.where(self.imagem_pb >= limiar, 255, 0).astype(np.uint8)
        imagem_binaria = Image.fromarray(binaria)
        imagem_binaria.save(caminho_saida)
        return imagem_binaria

    def equalizar_histograma(self, caminho_saida='equalizada.png'):
        hist, _ = np.histogram(self.imagem_pb.flatten(), bins=256, range=[0,256])
        cdf = hist.cumsum()
        cdf_normalizado = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
        cdf_normalizado = cdf_normalizado.astype(np.uint8)
        imagem_eq = cdf_normalizado[self.imagem_pb]
        imagem_final = Image.fromarray(imagem_eq)
        imagem_final.save(caminho_saida)
        return imagem_final
