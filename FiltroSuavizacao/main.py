import cv2
from imagem import Imagem

def main():
    img = cv2.imread("escadaria.png", cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Erro ao carregar a imagem.")
        return
    #Filtro aplicado utilizando a classe.
    filtro = Imagem(img, tamanho_janela=3)
    imagem_suavizada = filtro.aplicar()
    #Utilizando metodo para suavizar a imagem

    cv2.imwrite("saida_media.png", imagem_suavizada)
    cv2.imshow("Original", img)
    cv2.imshow("Suavizada", imagem_suavizada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()