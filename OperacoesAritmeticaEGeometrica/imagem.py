import numpy as np
from PIL import Image

class Imagem:
    def __init__(self, caminho_imagem):
        img = Image.open(caminho_imagem).convert("L")  # Converte para escala de cinza
        self.imagem = np.array(img, dtype=np.uint8)

    def salvar(self, array, nome_arquivo):
        img = Image.fromarray(array.astype(np.uint8))
        img.save(nome_arquivo)

    def adicao(self, outra):
        return np.clip(self.imagem + outra, 0, 255)

    def subtracao(self, outra):
        return np.clip(self.imagem - outra, 0, 255)

    def rotacao_90(self):
        # Rotação 90° horário: transpor + inverter linhas
        return np.flipud(self.imagem.T)
