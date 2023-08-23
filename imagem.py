from PIL import Image

class Imagem:
    def __init__(self, id, nome, caminho,extensao):
        self.id = id
        self.nome = nome
        self.caminho = caminho
        self.imagem = None
        self.extensao = extensao
        try:
            self.imagem = Image.open(self.caminho)
            print(f"Imagem: {self.nome} criada com sucesso")
        except Exception as e:
            print(f"Erro ao criar a imagem : {e}")

    def mostrar_imagem(self):
        try:
            self.imagem.show()
        except AttributeError:
            print("Imagem não encontrada ou não pode ser exibida.")