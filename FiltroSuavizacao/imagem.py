import numpy as np


class Imagem:
    def __init__(self, imagem, tamanho_janela=3):
        self.imagem = imagem.astype(np.float32)
        self.tamanho = tamanho_janela
        self.offset = tamanho_janela // 2

    def aplicar(self):
        h, w = self.imagem.shape
        resultado = np.zeros_like(self.imagem)

        # Padding com zeros
        imagem_padded = np.pad(self.imagem, self.offset, mode='constant', constant_values=0)

        for i in range(h):
            for j in range(w):
                # Extrai a vizinhança
                vizinhanca = imagem_padded[i:i+self.tamanho, j:j+self.tamanho]
                media = np.mean(vizinhanca)
                resultado[i, j] = media

        return resultado.astype(np.uint8)
        