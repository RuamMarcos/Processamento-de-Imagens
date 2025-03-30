import Imagem as Img

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


nova_img = Img.Imagem(matriz=matriz_de_num)
print("\nMatriz Original")
nova_img.imprimir_matriz()
print(f"Altura: {nova_img.altura}")
print(f"Largura: {nova_img.largura}")

print("\nMatriz reduzida:")
nova_img.vizinho_mp_reducao()
nova_img.imprimir_matriz()
print(f"Altura: {nova_img.altura}")
print(f"Largura: {nova_img.largura}")
