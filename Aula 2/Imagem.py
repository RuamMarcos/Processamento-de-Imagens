"""

Classe imagem

-> Comtem a matriz de pixels da imagem
-> largura e altura da imagem

Metodos (Ações):

-> bilinear_ampliacao: amplia a imagem por interpocao bilinear
-> bilinear_reducao: reduz a imagem por interpocao bilinear
-> vizinho_mp_ampliacao: amplia a imagem atraves da interpolacao do vizinho mais proximo
-> vizinho_mp_reducao: reduz a imagem atraves da interpolacao do vizinho mais proximo


"""
from random import randint as rd

matriz_de_num = []


# l = int(input("quantidade de linhas: "))
# c = int(input("quantiade de colunas: "))
c = l = 3

for j in range(c):
    linha = []
    for i in range(l):
        # linha.append(int(input(f"E[{j}][{i}]: ")))
        linha.append(rd(0, 20))
    matriz_de_num.append(linha)


class Imagem:
    def __init__(self, matriz: list[list[int]]):
        self.matriz = matriz
        self.largura = len(matriz[0])
        self.altura = len(matriz)

    def bilinear_ampliacao(self):
        for i in range(self.altura):
            j = 0
            while j < self.largura:
                self.matriz[i].insert(j+1, 0)
                j+=2

        

    def bilinear_reducao(self):
        pass

    def vizinho_mp_ampliacao(self):
        pass

    def vizinho_mp_reducao(self):
        pass

    def imprimir_matriz(self):
        for i in self.matriz:
            print(i)

nova_img = Imagem(matriz=matriz_de_num)
print("\nMatriz Original")
nova_img.imprimir_matriz()

print("\nMatriz ampliada em colunas:")
nova_img.bilinear_ampliacao()
nova_img.imprimir_matriz()