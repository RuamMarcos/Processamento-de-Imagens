from imagem import Imagem
import numpy as np

# Carrega imagens
img1 = Imagem("escadaria.png")
img2 = Imagem("escadaria_negativo.png")

# Garante mesmo tamanho (por segurança)
if img1.imagem.shape != img2.imagem.shape:
    raise ValueError("As imagens devem ter o mesmo tamanho.")

# Operações
soma = img1.adicao(img2.imagem)
sub = img1.subtracao(img2.imagem)
rot = img1.rotacao_90()

# Salva resultados
img1.salvar(soma, "saida_soma.png")
img1.salvar(sub, "saida_subtracao.png")
img1.salvar(rot, "saida_rotacao.png")
