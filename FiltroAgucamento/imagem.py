import numpy as np
import cv2
from scipy.signal import convolve2d

class Imagem:
    def __init__(self, caminho):
        self.original = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE).astype(np.float32)

    def aplicar_filtro(self, mascara, escalar=False):
        filtrada = convolve2d(self.original, mascara, mode='same', boundary='symm')
        if escalar:
            return self._escalar(filtrada)
        return np.clip(filtrada, 0, 255)

    def filtro_gradiente_sobel(self, escalar=False):
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
        sobel_y = np.array([[-1, -2, -1], [ 0,  0,  0], [ 1,  2,  1]], dtype=np.float32)

        gx = convolve2d(self.original, sobel_x, mode='same', boundary='symm')
        gy = convolve2d(self.original, sobel_y, mode='same', boundary='symm')

        gradiente = np.abs(gx) + np.abs(gy)
        if escalar:
            return self._escalar(gradiente)
        return np.clip(gradiente, 0, 255)

    def _escalar(self, imagem):
        min_val = np.min(imagem)
        max_val = np.max(imagem)
        if max_val - min_val == 0:
            return np.zeros_like(imagem)
        return ((imagem - min_val) / (max_val - min_val)) * 255
