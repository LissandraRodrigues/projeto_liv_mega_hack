# Projeto Liv - MEGA 3.0
# Autores: Luiza Lissandra R. Rosa e Iuri Lopes Almeida.
# Data: 05/07/2020
# Descrição: Programa que envia áudios de um livro (audiobook) para um ou mais usuários do Whatsapp.

# Importações.
from selenium import webdriver
import argparse
import time

# Define uma descrição sobre o que o programa faz.
parser = argparse.ArgumentParser(description = 'Envia capítulos de um livro como áudio pelo Whatsapp.')

parser.add_argument('-n', dest = 'nome_usuario', help = 'Nome do usuário que receberá o capítulo.')

args = parser.parse_args()

# Classe do ChatBot.
class whatsappBot:

    # Função inicial.
    def __init__(self):

        # Nome do grupo que contém o áudio do livro escolhido.
        self.audios = ["Dom Casmurro - Machado A."]

        options = webdriver.ChromeOptions()

        # Define que a linguagem é Português do Brasil.
        options.add_argument("lang = pt-br")

        # Driver do Chrome.
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver")

    # Função responsável por enviar o áudio.
    def enviaAudio(self):

        # Site que será aberto.
        self.driver.get("https://web.whatsapp.com/")

        # Coloca o programa para esperar por 10 segundos, enquanto a pessoa scannea o QRcode.
        time.sleep(10)

        # Para cada áudio inserido na lista de áudios.
        for audio in self.audios:

            # Encontra, por meio de HTML, o nome do grupo que contém o áudio nas conversas do Whatsapp.
            audio = self.driver.find_element_by_xpath(f"//span[@title = '{audio}']")

            # Coloca o programa para esperar por 3 segundo para evitar erros.
            time.sleep(3)

            # Clica no nome do grupo que contém o áudio.
            audio.click()

            # Coloca o programa para esperar por 3 segundos para evitar erros.
            time.sleep(3)

            # Encontra, por meio de HTML, a setinha de encaminhar mensagens.
            chat_bot = self.driver.find_element_by_class_name("_29g--")

            # Clica na setinha de encaminhar mensagens.
            chat_bot.click()

            # Coloca o programa para esperar por 3 segundos para evitar erros.
            time.sleep(3)

            # Encontra, por meio de HTML, o nome do usuário que receberá o áudio.
            pessoa = self.driver.find_element_by_xpath(f"//span[@title = '{args.nome_usuario}']")

            # Clica no usuário que receberá o áudio.
            pessoa.click()

            # Coloca o programa para esperar por 3 segundos para evitar erros.
            time.sleep(3)

            # Encontra, por meio de HTML, o botão de enviar.
            enviar = self.driver.find_element_by_xpath("/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/span/div/div/div")

            # Clica no botão de enviar.
            enviar.click()

            # Coloca o programa para esperar por 5 segundos para evitar erros.
            time.sleep(5)

bot = whatsappBot()

# Aciona a função que envia o áudio.
bot.enviaAudio()
