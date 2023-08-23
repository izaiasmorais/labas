class Biblioteca:
    def __init__(self) -> None:
        self.lista_de_imagens = []

    def adicionar_imagem(self, imagem):
        aux = self.buscar_imagem(imagem.nome)
        if(aux != None and imagem.nome == aux.nome): 
            return -1 
        self.lista_de_imagens.append(imagem)

    def remover_imagem(self, imagem):
        self.lista_de_imagens.remove(imagem)

    def listar_imagens(self):
        for imagem in self.lista_de_imagens:
            print(str(imagem.id+1) + ' - ' +imagem.nome) 

    def buscar_imagem(self, nome):
        for imagem in self.lista_de_imagens:
            if imagem.nome == nome:
                return imagem
        return None
    def buscar_imagem_id(self, id):
        for imagem in self.lista_de_imagens:
            if imagem.id == id:
                return imagem
        return None

    def mostrar_imagem(self, nome):
        imagem = self.buscar_imagem(nome)
        if imagem != None:
            imagem.mostrar_imagem()
        else:
            print("Imagem não encontrada.")