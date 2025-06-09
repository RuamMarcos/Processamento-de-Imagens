from PIL import Image
import Imagem as Img
import numpy as np

# Abra a imagem e converta para escala de cinza
img_path = "escadaria.png"  # Substitua pelo caminho da sua imagem
img_pil = Image.open(img_path).convert("L")

# Converta a imagem para matriz (lista de listas)
matriz_de_num = np.array(img_pil).tolist()

# Crie o objeto Imagem
nova_img = Img.Imagem(matriz=matriz_de_num)
print("\nMatriz Original")
nova_img.imprimir_matriz()
print(f"Altura: {nova_img.altura}")
print(f"Largura: {nova_img.largura}")

print("\nMatriz reduzida:")
nova_img.bilinear_reducao()
nova_img.imprimir_matriz()
print(f"Altura: {nova_img.altura}")
print(f"Largura: {nova_img.largura}")

# Converta a matriz reduzida de volta para imagem e salve
matriz_reduzida = np.array(nova_img.matriz, dtype=np.uint8)
img_reduzida = Image.fromarray(matriz_reduzida, mode="L")
img_reduzida.save("imagem_reduzida.png")
 