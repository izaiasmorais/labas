from PIL import ImageOps, ImageFilter

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