from PIL import ImageFilter

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
