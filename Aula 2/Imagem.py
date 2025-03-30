class Imagem:
    
    def __init__(self, matriz: list[list[int]]):
        self.matriz = matriz
        self.largura = len(matriz[0])
        self.altura = len(matriz)


    def bilinear_ampliacao(self):
        #Inserindo Colunas já atribuídas
        for i in range(self.altura):
            j = 0
            while j < self.largura:
                self.matriz[i].insert(j+1, round((self.getPixel(i, j)+self.getPixel(i, j+1))/2))
                j+=2

        #Inserindo linhas
        i = 0
        nova_linha = []
        while i < self.altura:
            for k in range(1, self.largura+1, 2):
                nova_linha.append(self.getPixel(i, k))
                d = self.getPixel(i, k-1) + self.getPixel(i, k+1) + self.getPixel(i+1, k-1) + self.getPixel(i+1, k+1) 
                d = round(d/4)
                nova_linha.append(d)
            nova_linha.append(self.getPixel(i, k))
                
            self.matriz.insert(i+1, nova_linha)
            i+=2
            nova_linha=[]

        #Atualizando atributos da imagem
        self.largura = len(self.matriz[0])
        self.altura = len(self.matriz)


    def bilinear_reducao(self):
        # Criando a nova matriz, essa vai ser uma versão reduzida da atual
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
        for i in range(0, self.altura):
            for j in range(0, self.largura,2):
                self.matriz[i].insert(j+1, self.getPixel(i, j))

        for i in range(0, self.altura, 2): 
            self.matriz.insert(i, self.matriz[i])
        
        self.altura = len(self.matriz)
        self.largura = len(self.matriz[0])
                

    def vizinho_mp_reducao(self):
        nova_matriz = []

        for i in range(0, self.altura, 2):
            nova_linha = []
            for j in range(0, self.largura, 2):
                # Obtém o pixel atual
                num = self.getPixel(i, j)
                count = 1

                # Verifica se existe linha abaixo
                if i + 1 < self.altura:
                    num += self.getPixel(i + 1, j)
                    count += 1
                # Verifica se existe coluna à direita
                if j + 1 < self.largura:
                    num += self.getPixel(i, j + 1)
                    count += 1
                # Verifica se existe diagonal inferior direita
                if i + 1 < self.altura and j + 1 < self.largura:
                    num += self.getPixel(i + 1, j + 1)
                    count += 1

                # Calcula a média dos pixels vizinhos
                num = round(num / count)
                nova_linha.append(num)

            nova_matriz.append(nova_linha)

        # Atualiza a matriz e os atributos
        self.matriz = nova_matriz
        self.altura = len(nova_matriz)
        self.largura = len(nova_matriz[0])


    def imprimir_matriz(self):
        for i in self.matriz:
            print(i)

    def getPixel(self, i, j):
        return self.matriz[i][j]
