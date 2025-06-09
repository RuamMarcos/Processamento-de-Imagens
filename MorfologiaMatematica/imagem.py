# imagem.py
import numpy as np
##EE - Notação para Mascara
class Imagem:
    def __init__(self, matriz):
        self.imagem = matriz.astype(int)

    def _pad(self, matriz, ee):
        """Adiciona borda (padding) para suportar deslocamento do elemento estruturante"""
        pad_h = ee.shape[0] // 2
        pad_w = ee.shape[1] // 2
        return np.pad(matriz, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

    def erosao(self, ee):
        
        img_padded = self._pad(self.imagem, ee)
        output = np.zeros_like(self.imagem)

        for i in range(output.shape[0]):
            for j in range(output.shape[1]):
                region = img_padded[i:i+ee.shape[0], j:j+ee.shape[1]]
                if np.array_equal(region * ee, ee):  #região contém o EE totalmente
                    output[i, j] = 1
        self.imagem = output

    def dilatacao(self, ee):
     
        img_padded = self._pad(self.imagem, ee)
        output = np.zeros_like(self.imagem)

        for i in range(output.shape[0]):
            for j in range(output.shape[1]):
                region = img_padded[i:i+ee.shape[0], j:j+ee.shape[1]]
                if np.any(region * ee):  #qualquer sobreposição com EE
                    output[i, j] = 1
        self.imagem = output

    def abertura(self, ee):
        self.erosao(ee)
        self.dilatacao(ee)

    def fechamento(self, ee):
        self.dilatacao(ee)
        self.erosao(ee)

    def get_imagem(self):
        return (self.imagem * 255).astype(np.uint8)