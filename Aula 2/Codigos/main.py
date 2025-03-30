import Imagem as Img

from random import randint as rd

nova_imagem = Img.Imagem("../imagens/flores.jpg")
nova_imagem.bilinear_ampliacao()
nova_imagem.salvar("passaros_reduzida.jpg")