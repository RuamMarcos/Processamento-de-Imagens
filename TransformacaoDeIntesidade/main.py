#A função escolhida foi a transformação em negativo.

from imagem import Imagem

def main():
    caminho = "escadaria.png"  
    img = Imagem(caminho)
    imagem_negativa = img.transformar_negativo()
    imagem_negativa.show()
    imagem_negativa.save("saida.png")

if __name__ == "__main__":
    main()
