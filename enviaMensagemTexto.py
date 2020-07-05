# Projeto Liv - Mega Hack 3.0
# Autores: Luiza Lissandra R. Rosa e Iuri Lopes Almeida.
# Data: 05/07/2020
# Descrição: Programa que envia os capítulos de um livro para um ou mais usuários do Whatsapp.

# Importações.
from selenium import webdriver
import argparse
import time

# Define uma descrição sobre o que o programa faz.
parser = argparse.ArgumentParser(description = 'Envia um capítulo de um livro como mensagens de texto pelo Whatsapp.')

parser.add_argument('-c', dest = 'numero_capitulo', help = 'Número do capítulo desejado.')

parser.add_argument('-n', dest = 'nome_usuario', help = 'Nome do usuário que receberá o capítulo.')

args = parser.parse_args()

# Classe do ChatBot.
class whatsappBot:

    # Função inicial.
    def __init__(self):

        # Caminho para o Livro Dom Casmurro - Machado de Assis.
        livro = open("domCasmurro.txt")

        # Lê todas as linhas do arquivo txt.
        leitura = livro.readlines()

        # Variável que armazena as linhas que formam o parágrafo.
        paragrafo = ""

        # Lista que possui como elementos os paragráfos.
        capitulo = []

        # Lista que possui como elementos uma lista de capítulos.
        capitulos = []

        # Variável auxiliar necessária para o primeiro capítulo.
        auxiliar = 1

        # Para cada frase contida em leitura.
        for frase in leitura:

            # Verifica se na frase existe a palavra "CAPÍTULO", pois é ela que separa os capítulos.
            # O auxiliar é para o primeiro capítulo ser pego.
            if (("CAPÍTULO" in frase) == False) or auxiliar == 1:

                # Se auxiliar for igual a 1 é porque esse é o primeiro capítulo.
                if auxiliar == 1:

                    # Adiciona antes de tudo, o nome do livro e autor.
                    paragrafo += "Dom Casmurro - Machado de Assis\n"

                # Se o tamanho da frase for diferente de 1.
                if len(frase) != 1:

                    # Substitui a quebra de linha por um espaço.
                    fraseEditada = frase.replace("\n", " ")

                    # Adiciona a frase editada ao parágrafo.
                    paragrafo += fraseEditada

                # Se o tamanho da frase for igual 1 é porque há apenas uma quebra de linha
                # que revela a finalização do parágrafo.
                else:

                    # Adiciona o parágrafo ao capítulo.
                    capitulo += paragrafo

                    # Dá a quebra de linha necessária para separar os parágrafos.
                    paragrafo = "\n\n"

            # Ao encontrar a palavra "CAPÍTULO", que indica o término do capítulo anterior.
            else:

                # Adiciona o capítulo à lista de capítulos.
                capitulos += [capitulo]

                # Adiciona o nome do próximo e uma quebra de linha.
                capitulo = frase + "\n"
            
            # Para que o if, após inserção do primeiro capítulo, só funcione quando a primeira condição for verdadeira.
            auxiliar = 2

        # Primeiro capítulo do livro.
        self.mensagem = capitulos[int(args.numero_capitulo) - 1]
        
        # Usuário que receberá o primeiro capítulo do livro.
        self.usuarios = [args.nome_usuario]

        options = webdriver.ChromeOptions()

        # Define que a linguagem é Português do Brasil.
        options.add_argument("lang = pt-br")

        # Driver do Chrome.
        self.driver = webdriver.Chrome(executable_path = r"./chromedriver")

    # Função responsável por enviar as mensagens.
    def enviarMensagem(self):

        # Site que será aberto.
        self.driver.get("https://web.whatsapp.com/")

        # Coloca o programa para esperar por 10 segundos, enquanto a pessoa scannea o QRcode.
        time.sleep(10)

        # Para cada usuário inserido na lista de usuários.
        for usuario in self.usuarios:

            # Encontra, por meio de HTML, o nome dele nas conversas do Whatsapp.
            usuario = self.driver.find_element_by_xpath(f"//span[@title = '{usuario}']")

            # Coloca o programa para esperar por 3 segundos para evitar erros.
            time.sleep(3)

            # Clica no nome do usuário.
            usuario.click()

            # Encontra, por meio de HTML, a caixa de mensagem.
            chat_bot = self.driver.find_element_by_class_name("_3uMse")

            # Coloca o programa para esperar por 3 segundos para evitar erros.
            time.sleep(3)

            # Clica na caixa de mensagem.
            chat_bot.click()

            # Escreve os parágrafos do capítulo.
            chat_bot.send_keys(self.mensagem)

            # Coloca o programa para esperar por 5 segundos para evitar erros.
            time.sleep(5)

bot = whatsappBot()

# Aciona a função que envia os capítulos.
bot.enviarMensagem()
