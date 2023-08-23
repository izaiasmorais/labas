from imagem import Imagem  
from download import Download
from biblioteca import Biblioteca
from filtros import Filtro_foto_negativa, Filtro_contorno, Filtro_blurred, Filtro_escala_cinza, Filtro_Cartoon,Filtro_preto_branco
from urllib.parse import urlparse
import copy
import sys
import os

class main:
    def __init__(self) -> None:
        self.biblioteca = Biblioteca()
        self.adiciona_imagem_existente()
    
    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def adiciona_imagem_existente(self):
        arquivos = os.listdir(os.getcwd())
        imagens = [arquivo for arquivo in arquivos if arquivo.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        for imagem in imagens:
            img = Imagem(id=len(self.biblioteca.lista_imagens), nome=imagem, caminho=imagem, extensao=os.path.splitext(imagem)[1])
            self.biblioteca.adicionar_imagem(img)
            self.limpar_terminal()

    def exibir_menu(self):
        while True:
            print("\n1. Informar a URL da imagem")
            print("2. Aplicar filtro na imagem")
            print("3. Listar os arquivos de imagens")
            print("4. Remover imagem(s)")
            print("5. Remover conjunto de imagens")
            print("0. Sair")
            opcao = input('Digite a opção desejada: ')
            if opcao == "1":
                url = input("Digite a url da imagem: ")
                self.limpar_terminal()
                self.cria_imagem(url)
            elif opcao == "2":
                self.limpar_terminal()
                self.aplicar_filtro()
            elif opcao == "3":
                self.limpar_terminal()
                self.listar_arquivos()
            elif opcao == "4":
                self.limpar_terminal()
                self.remover_imagem()
            elif opcao == "5":
                self.limpar_terminal()
                self.remover_conjunto_imagens()
            elif opcao == "0":
                print("Saindo...")
                self.biblioteca.limpa_sistema()
                sys.exit()
            else:
                print("Opção inválida")
            
    
    def cria_imagem(self, url_passada):
        url = url_passada

        parsed_url = urlparse(url)
        caminho_arquivo = parsed_url.path
        nome_arquivo, extensao = os.path.splitext(os.path.basename(caminho_arquivo))
        nome_final = nome_arquivo + extensao

        md = Download( url_or_caminho= url, caminho= nome_final)
        resposta = md.baixar_imagem()
        img = Imagem(id = len(self.biblioteca.lista_imagens), nome = nome_final,caminho = nome_final, extensao = extensao)

        if resposta is True:
            self.biblioteca.adicionar_imagem(img)
    
    def aplicar_filtro(self):
        self.limpar_terminal()
        if len(self.biblioteca.lista_imagens) == 0:
            print("Não é possível aplicar filtro!")
            print("Não há imagens na biblioteca.")
            return
        print("\nEscolha a imagem que deseja aplicar o filtro:")
        self.biblioteca.listar_imagens()

        id = input("\nDigite o numero da imagem:")
        imagem = copy.deepcopy(self.biblioteca.buscar_imagem_id(int(id)-1))
        
        if imagem != None:
            print("\n1. Filtro Preto e Branco\n2. Filtro Escala de Cinza\n3. Filtro Cartoon\n4. Filtro Foto Negativa\n5. Filtro Contorno\n6. Filtro Blurred\n7. Voltar para o menu \n")
            opcao = input('Digite a opção desejada:')
            if opcao == "1":
                filtro = Filtro_preto_branco()
            elif opcao == "2":
                filtro = Filtro_escala_cinza()
            elif opcao == "3":
                filtro = Filtro_Cartoon()
            elif opcao == "4":
                filtro = Filtro_foto_negativa()
            elif opcao == "5":
                filtro = Filtro_contorno()
            elif opcao == "6":
                filtro = Filtro_blurred()
            elif opcao == "7":
                self.exibir_menu()
            else:
                print("Opção inválida")
                self.aplicar_filtro()

            imagem.nome = imagem.nome[:-4] + "_" + type(filtro).__name__+ imagem.extensao
            imagem.imagem = filtro.aplicar_filtro(imagem.imagem)
            imagem.id = len(self.biblioteca.lista_imagens)
                
            imagem.imagem.save(imagem.nome)
            imagem.mostrar_imagem()
                
            self.biblioteca.adicionar_imagem(imagem)
        else:
            print("Opção inválida")    

    def remover_imagem(self):
        if len(self.biblioteca.lista_imagens) == 0:
            print("Não é possível remover a imagem!")
            print("Não há imagens na biblioteca.")
            return
        print("Escolha a imagem que deseja remover:")
        self.biblioteca.listar_imagens()
        id = "0"
        while int(id) < 1:
            id = input("Digite o numero da imagem:")
            if int(id) == 0:
                self.exibir_menu()
            if int(id) < 1 or len(id) < 1:
                print("Opção inválida!")
                id = "0"
        imagem = None
        for imagem_lib in self.biblioteca.lista_imagens:
            if imagem_lib.id == int(id)-1:
                imagem = imagem_lib
        if imagem == None:
            print("Opção inválida")
            self.remover_imagem()
        imagem = copy.deepcopy(self.biblioteca.buscar_imagem_id(int(id)-1))
        self.biblioteca.remover_imagem(imagem)
        self.exibir_menu()

    def remover_conjunto_imagens(self):
        print("Escolha o conjunto de imagens a ser removido:")
        print("1. Excluir imagens carregadas pelo usuário")
        print("2. Excluir imagens criadas a partir da aplicação de filtros")
        print("3. Excluir todas as imagens")
        print("0. Voltar ao menu")
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            self.biblioteca.remover_imagens_por_tipo("URL")
        elif opcao == "2":
            self.biblioteca.remover_imagens_por_tipo("Filtro")
        elif opcao == "3":
            self.biblioteca.remover_todas_imagens()
        elif opcao == "0":
            self.exibir_menu()
        else:
            print("Opção inválida")

    def listar_arquivos(self):
        if len(self.biblioteca.lista_imagens) == 0:
            print("Não foi possível listar as imagens!")
            print("Não há imagens na biblioteca.")
            return
        print("Lista de imagens:")
        self.biblioteca.listar_imagens()
        self.exibir_menu()

if __name__ == '__main__':
    main().exibir_menu()
