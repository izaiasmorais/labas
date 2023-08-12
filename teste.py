import requests
from PIL import Image
import shutil
import os


class Download:
    def __init__(self, url_or_caminho, caminho):
        self.url_or_caminho = url_or_caminho
        self.caminho_do_arquivo = caminho

    def baixar_imagem(self):
        try:
            if self.url_or_caminho.startswith(("http://", "https://", "ftp://")):
                # Se a URL for remota, faz o download
                response = requests.get(self.url_or_caminho)
                response.raise_for_status()
                with open(self.caminho_do_arquivo, "wb") as file:
                    file.write(response.content)
            else:
                # Se a URL for um caminho local, copia o arquivo para o caminho de destino
                shutil.copy(self.url_or_caminho, self.caminho_do_arquivo)
            print(
                f"Download realizado com sucesso, salvo em: {self.caminho_do_arquivo}"
            )
        except requests.exceptions.MissingSchema:
            print("URL inválida.")
        except requests.exceptions.RequestException as e:
            print(f"Erro na conexão: {e}")
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {self.url_or_caminho}")


class Imagem:
    def __init__(self, id, nome, caminho):
        self.id = id
        self.nome = nome
        self.caminho = caminho
        self.imagem = None
        try:
            self.imagem = Image.open(self.caminho)
            print(f"Imagem: {self.nome} criada com sucesso")
        except Exception as e:
            print("Erro ao criar a imagem")

    def mostrar_imagem(self):
        try:
            self.imagem.show()
        except AttributeError:
            print("Imagem não encontrada ou não pode ser exibida.")


class Biblioteca:
    def __init__(self) -> None:
        self.lista_de_imagens = []

    def adicionar_imagem(self, imagem):
        self.lista_de_imagens.append(imagem)

    def remover_imagem(self, imagem):
        self.lista_de_imagens.remove(imagem)

    def listar_imagens(self):
        print("Lista de imagens:")
        for imagem in self.lista_de_imagens:
            print(f"{imagem.id}-{imagem.nome}")

    def buscar_imagem(self, nome):
        for imagem in self.lista_de_imagens:
            if imagem.nome == nome:
                return imagem
        return None

    def mostrar_imagem(self, nome):
        imagem = self.buscar_imagem(nome)
        if imagem != None:
            imagem.mostrar_imagem()
        else:
            print("Imagem não encontrada.")


url = "https://i2-prod.football.london/incoming/article25783675.ece/ALTERNATES/s1200c/0_GettyImages-1450108295.jpg"
caminho = "messi.png"
md = Download(url, caminho)
md.baixar_imagem()
imagemteste1 = Imagem(1, "MessiWC", caminho)

url = "https://dynaimage.cdn.cnn.com/cnn/c_fill,g_auto,w_1200,h_675,ar_16:9/https%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F180404103656-cristiano-ronaldo-overhead-kick-real-madrid-goal.jpg"
caminho = "cristiano.png"
md = Download(url, caminho)
md.baixar_imagem()
imagemteste2 = Imagem(2, "CristianoUCL", caminho)

url = "https://images.livemint.com/img/2022/12/11/1600x900/Neymar_Jr_1670779710460_1670779710605_1670779710605.JPG"
caminho = "Neymar.png"
md = Download(url, caminho)
md.baixar_imagem()
imagemteste3 = Imagem(3, "neymarWC", caminho)

bibi = Biblioteca()
bibi.adicionar_imagem(imagemteste1)
bibi.adicionar_imagem(imagemteste2)
bibi.adicionar_imagem(imagemteste3)
bibi.listar_imagens()
