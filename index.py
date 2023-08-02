import requests
from io import BytesIO
from PIL import Image


class Manipulador:
    def __init__(self, url):
        self.url = url

    def baixar_imagem(self):
        resposta = requests.get(self.url)
        if resposta.status_code == 200:
            return resposta.content
        else:
            print(
                f'Ocorreu um erro ao tentar baixar a imagem da URL: {self.url}')
            return None

    def salvar_imagem(self):
        dados_da_imagem = self.baixar_imagem()
        if (dados_da_imagem):
            with open("image.jpg", 'wb') as f:
                f.write(dados_da_imagem)
                print('Imagem salva com sucesso em URL: imagem.jpg')
        else:
            print('Não foi possível salvar a imagem')


teste = Manipulador("https://i.imgur.com/4JfFzfh.png")

teste.salvar_imagem()
