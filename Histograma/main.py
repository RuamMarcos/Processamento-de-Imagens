from imagem import Imagem
import matplotlib.pyplot as plt

def main():
    caminho = 'escadaria.png'  # Substitua pelo caminho correto
    img = Imagem(caminho)

    # Mostra a imagem original
    img.mostrar_imagem(img.img_original, "Imagem Original")

    # Equalização do histograma
    img_equalizada, hist, cdf_normalizado = img.equalizar_histograma()

    # Mostra a imagem equalizada
    img.mostrar_imagem(img_equalizada, "Imagem Equalizada")

    # Plot do histograma original e da CDF
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(hist, color='black')
    plt.title("Histograma Original")

    plt.subplot(1, 2, 2)
    plt.plot(cdf_normalizado, color='red')
    plt.title("Função de Distribuição Acumulada (CDF)")

    plt.show()

if __name__ == "__main__":
    main()
 