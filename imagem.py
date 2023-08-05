from PIL import Image
class Imagem:
    def __init__(self, id, nome, caminho):
        self.id = id
        self.nome = nome
        self.caminho = caminho
        self.imagem = None
        try:
            image.open(self.caminho)
        except Exception as e:
            print("Erro ao criar a imagem")

    def mostrar_imagem(self):
        Image.open(self.camimho).show()
