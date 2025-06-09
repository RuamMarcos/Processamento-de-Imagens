import cv2
import numpy as np
from imagem import Imagem
import os
def main():
    # Carrega a imagem em escala de cinza
   
    img_path = "escadaria.png"  # Caminho para a imagem
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Erro: Imagem não encontrada.")
        return

    # Converte a imagem para binária 
    _, binaria = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)

    # Elemento estruturante 3x3
    ee = np.ones((3, 3), dtype=int)

    # Abertura
    img_aberta = Imagem(binaria.copy())
    img_aberta.abertura(ee)
    cv2.imwrite("saida_abertura.png", img_aberta.get_imagem())

    # Fechamento
    img_fechada = Imagem(binaria.copy())
    img_fechada.fechamento(ee)
    cv2.imwrite("saida_fechamento.png", img_fechada.get_imagem())

    
    cv2.imshow("Original", binaria * 255)
    cv2.imshow("Abertura", img_aberta.get_imagem())
    cv2.imshow("Fechamento", img_fechada.get_imagem())
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()