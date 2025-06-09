from imagem import Imagem
import matplotlib.pyplot as plt

def main():
    caminho = 'image.png'  # Substitua pelo caminho da sua imagem
    img = Imagem(caminho)

    print("Exibindo histograma da imagem original...")
    img.exibir_histograma()

    limiar = img.encontrar_limiar_metodo_vale()
    print(f"Limiar encontrado: {limiar}")

    print("Salvando imagem segmentada...")
    img_segmentada = img.limiarizar(limiar, 'imagem_segmentada.png')

    print("Salvando imagem equalizada...")
    img_equalizada = img.equalizar_histograma('imagem_equalizada.png')

    print("Processo concluído com sucesso.")

if __name__ == "__main__":
    main()
