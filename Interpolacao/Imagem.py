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
import numpy as np

class Imagem:
    def __init__(self, matriz: list[list[int]]):
        self.matriz = matriz
        self.largura = len(matriz[0])
        self.altura = len(matriz)


    def bilinear_ampliacao(self):
        #Inserindo Colunas 
        for i in range(self.altura):
            j = 0
            while j < self.largura:
                self.matriz[i].insert(j+1, round((self.getPixel(i, j)+self.getPixel(i, j+1))/2))
                j+=2

        #Inserindo linhas
        i = 0
        novas_linhas = []
        while i < self.altura:
            for k in range(1, self.largura+1, 2):
                novas_linhas.append(self.getPixel(i, k))
                d = self.getPixel(i, k-1) + self.getPixel(i, k+1) + self.getPixel(i+1, k-1) + self.getPixel(i+1, k+1) 
                d = round(d/4)
                novas_linhas.append(d)
            novas_linhas.append(self.getPixel(i, k))
                
            self.matriz.insert(i+1, novas_linhas)
            i+=2
            novas_linhas=[]

        #Atualizando atributos da imagem
        self.largura = len(self.matriz[0])
        self.altura = len(self.matriz)


    def bilinear_reducao(self):
        nova_matriz = []

        for j in range(0, self.altura, 2):
            nova_linha = []
            for i in range(0, self.largura, 2):
                # Verifica se os índices estão dentro dos limites
                soma = self.getPixel(j, i)
                count = 1

                if i + 1 < self.largura:  # Verifica se existe coluna à direita
                    soma += self.getPixel(j, i + 1)
                    count += 1
                else:
                    #Se não existe coluna a direita, ele duplica a coluna atual para a direita
                    soma += self.getPixel(j, i)
                    count += 1

                if j + 1 < self.altura:  # Verifica se existe linha abaixo
                    soma += self.getPixel(j + 1, i)
                    count += 1
                else:
                    #Se não existe linha a baixo, ele duplica a linha atual para baixo
                    soma += self.getPixel(j, i)
                    count += 1

                if i + 1 < self.largura and j + 1 < self.altura:  # Verifica diagonal inferior direita
                    soma += self.getPixel(j + 1, i + 1)
                    count += 1

                # Calcula a média dos pixels vizinhos
                elemento = round(soma / count)
                nova_linha.append(elemento)
                
            nova_matriz.append(nova_linha)

        # Atualiza a matriz e os atributos
        self.matriz = nova_matriz
        self.altura = len(nova_matriz)
        self.largura = len(nova_matriz[0])


    def vizinho_mp_ampliacao(self):
        h, w = self.matriz.shape
        ampliada = np.zeros((h * 2, w * 2), dtype=np.uint8)

        for y in range(h):
            for x in range(w):
                valor = self.matriz[y, x]
                ampliada[y*2:y*2+2, x*2:x*2+2] = valor  # Replica o pixel 2x2
        return ampliada

    def vizinho_mp_reducao(self):
        # Elimina linhas e colunas ímpares (1, 3, 5,...)
        reduzida = self.matriz[::2, ::2]
        return reduzida

    

    def imprimir_matriz(self):
        for i in self.matriz:
            print(i)

    def getPixel(self, i, j):
        return self.matriz[i][j]
