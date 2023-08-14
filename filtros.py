#from PIL import Image
from PIL import ImageOps, ImageFilter

#Os filtros disponíveis são: Escala de Cinza, Preto e Branco, Filtro Cartoon, Modo Foto
#Negativa (inversão das cores da imagem), Modo Contorno e Modo Blurred.

class Filtro_preto_branco:
    def aplicar_filtro(self, image):
        grayscale_image = image.convert("L")
        black_white_image = grayscale_image.convert("1")
        return black_white_image

class Filtro_escala_cinza:
    def aplicar_filtro(self, image):
        grayscale_image = image.convert("L")
        return grayscale_image

        
    
class Filtro_Cartoon:
    def aplicar_filtro(self, image):           #Filtro Cartoon(Emboss) que muito parece um relevo
        cartooned_image = image.filter(ImageFilter.EMBOSS)
        return cartooned_image
    
class Filtro_foto_negativa:
    def aplicar_filtro(self, image):
        negativo_image = ImageOps.invert(image)
        return negativo_image
    
class Filtro_contorno:
    def aplicar_filtro(self, image):
        contornada_image = image.filter(ImageFilter.CONTOUR)
        return contornada_image
    
class Filtro_blurred:
    def aplicar_filtro(self, image):
        blurred_image = image.filter(ImageFilter.BLUR)
        return blurred_image




#                              ↑ ↑  ENTIDADE  ↑ ↑


#                              ↓ ↓  CONTROLE  ↓ ↓
'''
class Main:
    def __init__(self, utilidades):
        self.utilidades = utilidades

    def minha_funcao(self, minha_url):
        print(f'URL: {minha_url}')
        # add an indented block here
        if minha_url:
            print("URL is not empty")
        else:
            print("URL is empty")
    nome_arquivo, extensao_arquivo = self.utilidades.extrair_nome_extensao_url(minha_url)
    arquivo = nome_arquivo + extensao_arquivo
    print(f'Arquivo: {arquivo}')
    meu_download = Download(url=minha_url, path_arquivo=arquivo)
    print(f'Inicia download...')
    meu_download.download_file()
    print(f'Download concluído!')
    self.utilidades.wait_for_file(arquivo)
    imagem_teste = Imagem(id=1, nome_arquivo=arquivo, path_arquivo=arquivo)
    print(imagem_teste)
    return imagem_teste.conteudo()
'''







'''
testando
from PIL import ImageOps, ImageFilter
from download import*
from imagem import*

url = "https://i2-prod.football.london/incoming/article25783675.ece/ALTERNATES/s1200c/0_GettyImages-1450108295.jpg"
caminho = "messi.png"
md = Download(url, caminho)
md.baixar_imagem()
imagemteste1 = Imagem(1, "MessiWC", caminho)
blurred = Filtro_blurred()
messiblrrd = blurred.aplicar_filtro(imagemteste1.imagem)
messiblrrd.show()
'''