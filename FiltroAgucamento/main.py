import matplotlib.pyplot as plt
from imagem import Imagem

laplacian_masks = [
    [[ 0,  1,  0],
     [ 1, -4,  1],
     [ 0,  1,  0]],

    [[ 1,  1,  1],
     [ 1, -8,  1],
     [ 1,  1,  1]],

    [[ 0, -1,  0],
     [-1,  4, -1],
     [ 0, -1,  0]],

    [[-1, -1, -1],
     [-1,  8, -1],
     [-1, -1, -1]]
]

def mostrar_resultados(imagem, titulo, imagens):
    plt.figure(figsize=(15,5))
    for i, img in enumerate(imagens):
        plt.subplot(1, len(imagens), i+1)
        plt.imshow(img, cmap='gray')
        plt.title(f'{titulo} {i+1}')
        plt.axis('off')
    plt.tight_layout()
    plt.show()

def main():
    caminho = 'escadaria.png'  # Substitua pelo caminho da sua imagem
    img = Imagem(caminho)

    resultados_laplaciano = [img.aplicar_filtro(m, escalar=True) for m in laplacian_masks]
    mostrar_resultados(img.original, 'Laplaciano', resultados_laplaciano)

    gradiente = img.filtro_gradiente_sobel(escalar=True)
    plt.figure(figsize=(5,5))
    plt.imshow(gradiente, cmap='gray')
    plt.title('Gradiente Sobel')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()
