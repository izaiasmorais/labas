import requests
import shutil


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
