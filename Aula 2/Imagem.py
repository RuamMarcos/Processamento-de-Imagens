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
        pass

    def vizinho_mp_ampliacao(self):
        pass

    def vizinho_mp_reducao(self):
        pass

    def imprimir_matriz(self):
        for i in self.matriz:
            print(i)

    def getPixel(self, i, j):
        return self.matriz[i][j]
