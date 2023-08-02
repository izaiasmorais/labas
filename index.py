import requests
from PIL import Image


class Manipulador:

    def __init__(self, url):
        self.url = url

    def baixar_imagem(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            with open("imagem.jpg", 'wb') as file:
                file.write(response.content)
                print('Imagem salva com sucesso em URL: imagem.jpg')
        except requests.exceptions.MissingSchema:
            print("URL inválida.")
        except requests.exceptions.RequestException as e:
            print(f"Erro na conexão: {e}")

    def mostrar_imagem(self):
        Image.open("imagem.jpg").show()


manipulador = Manipulador("https://i.imgur.com/4JfFzfh.png")

manipulador.baixar_imagem()

manipulador.mostrar_imagem()
