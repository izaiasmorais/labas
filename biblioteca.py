import os

class Biblioteca:
    def __init__(self) -> None:
        self.lista_imagens = []

    def adicionar_imagem(self, imagem):
        aux = self.buscar_imagem(imagem.nome)
        if(aux != None and imagem.nome == aux.nome): 
            return -1 
        self.lista_imagens.append(imagem)

    def remover_imagem(self, imagem):
        for imagem_lib in self.lista_imagens:
            if imagem_lib.id == imagem.id:
                self.remover_arquivo(imagem_lib.nome)
                self.lista_imagens.remove(imagem_lib)

    def listar_imagens(self):
        for imagem in self.lista_imagens:
            print(str(imagem.id+1) + ' - ' +imagem.nome)

    def buscar_imagem(self, nome):
        for imagem in self.lista_imagens:
            if imagem.nome == nome:
                return imagem
        return None
    def buscar_imagem_id(self, id):
        for imagem in self.lista_imagens:
            if imagem.id == id:
                return imagem
        return None

    def mostrar_imagem(self, nome):
        imagem = self.buscar_imagem(nome)
        if imagem != None:
            imagem.mostrar_imagem()
        else:
            print("Imagem não encontrada.")

    def limpa_sistema(self):
        for imagem in self.lista_imagens:
            self.remover_arquivo(imagem.nome)

    def remover_imagens_por_tipo(self, tipo):
        imagens_removidas = []
        for imagem in self.lista_imagens:
            if tipo == "Filtro":
                if "_Filtro_" in imagem.nome:
                    imagens_removidas.append(imagem)
            elif tipo == "URL":
                if "_Filtro_" not in imagem.nome:
                    imagens_removidas.append(imagem)

        for imagem in imagens_removidas:
            self.remover_arquivo(imagem.nome)
            self.lista_imagens.remove(imagem)
        print(f"Removidas {len(imagens_removidas)} imagens")

    def remover_todas_imagens(self):
        for imagem in self.lista_imagens:
            self.remover_arquivo(imagem.nome)
        self.lista_imagens = []
        print("Todas as imagens foram removidas.")

    def remover_arquivo(self, nome_arquivo):
        try:
            os.remove(nome_arquivo)
            print(f"Arquivo {nome_arquivo} removido com sucesso.")
        except OSError as e:
            print(f"Erro ao remover o arquivo {nome_arquivo}: {e}")