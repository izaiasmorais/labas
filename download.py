import requests
from PIL import Image

class Download:

    def __init__(self, url, caminho):
        self.url = url
        self.caminho_do_arquivo = caminho

    def baixar_imagem(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            with open(self.caminho_do_arquivo, 'wb') as file:
                file.write(response.content)
                print(f'Imagem salva com sucesso em URL: {self.caminho_do_arquivo}')
        except requests.exceptions.MissingSchema:
            print("URL inválida.")
        except requests.exceptions.RequestException as e:
            print(f"Erro na conexão: {e}")

    def mostrar_imagem(self):
        Image.open("imagem.jpg").show()
