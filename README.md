# Liv - Mega Hack 3.0

Meu time e eu escolhemos o desafio da <a href = "https://arvoreeducacao.com.br/"> Árvore Educação </a> inserido no <a href = "https://www.megahack.com.br/"> Mega Hack </a>.

Nossa solução consiste em uma aplicação web que permite o usuário ler ou ouvir livros pelo aplicativo Whatsapp.

* Página inicial.

![alt text](https://github.com/LissandraRodrigues/projeto_liv_mega_hack/blob/master/pagina_inicial.png?raw=true)

* Página do Livro Dom Casmurro de Machado de Assis.

![alt text](https://github.com/LissandraRodrigues/projeto_liv_mega_hack/blob/master/pagina_dom_casmurro.png?raw=true)

# Descrição

* Site 

No site do Liv, o usuário escolhe o livro que deseja ler, digita o número do celular, a quantidade de capítulos que quer receber por dia, o horário que quer recebê-los e o formato de leitura desejado.

* Leitura no WhatsApp

O programa faz a leitura de um arquivo txt que contém o livro Dom Casmurro de Machado de Assis (escolhemos este livro para a demonstração). Após a leitura, o programa separa o livro em capítulos e envia esses capítulos pelo WhatsApp no formato de mensagem de texto. Cada uma das mensagens enviadas é um parágrafo do capítulo.

<b>Obs.:</b> O livro utilizado foi encontrado no formato de pdf <a href = "http://machado.mec.gov.br/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=20&order=year&searchword=dom+casmurro&Itemid=668">nesta página</a> do Ministério da Educação e foi convertido para a extensão txt utilizando <a href = "https://convertio.co/pt/pdf-txt/"> esta </a> ferramenta online.

* Audiobook no Whatsapp

O programa acessa o Whatsapp, entra em um grupo específico do livro escolhido e encaminha, ao usuário que solicitou, o áudio. 

<b>Obs. 1:</b> O grupo referido acima é feito dentro do aplicativo Whatsapp antes da execução do programa e contém o áudio do livro. 

<b>Obs. 2:</b> O áudio utilizado pode ser encontrado <a href = "https://forum.librivox.org/viewtopic.php?f=28&t=74712"> nesta página </a>.

<b>Obs. 3:</b> A parte da solução responsável por converter os livros em mensagens de texto e áudios no Whatsapp foi escrita na linguagem Python e usa a biblioteca <a href = "https://selenium-python.readthedocs.io/"> Selenium </a> como base.

# Como funciona?

O usuário entra no site, escolhe o livro que quer ler, opta por áudio ou mensagem de texto, cadastra o número de celular e recebe o livro no formato escolhido em seu celular. Para mais detalhes acesse esse <a href = "https://www.youtube.com/watch?v=lmYbyudkgS0&feature=youtu.be"> vídeo </a> de demonstração.

# Instalação

É preciso ter o Python instalado no seu computador (<a href = "https://www.python.org/downloads/">Python </a>, recomendado baixar a última versão). Para importar algumas funções usadas nesse projeto é preciso fazer a instalação de uma biblioteca:

* selenium - Forma de instalação: <b>pip install selenium</b>

<b>Obs 01.:</b> É também necessário o uso do ChromeDriver 83.0.4103.39 que pode ser baixado <a href = "https://chromedriver.chromium.org/downloads"> nesta página </a>. Ele deve ser inserido na mesma pasta do projeto, entretanto ele já está inserido neste repositório.

# Uso 

Após as instalações, para começar usar é preciso clonar esse repositório e seguir alguns parâmetros que serão passados pela linha de comando (terminal):

* Para receber o livro como mensagem de texto:
    
    * python enviaMensagemTexto.py -c <Número do Capítulo> -n <Nome do usuário que você enviará o livro (tem que ser exatamente igual ao que está no WhatsApp)>
    
        Exemplo: python enviaMensagemTexto.py -c 19 -n João
        
        <b>Obs.:</b> Para demonstração, utilizamos o livro Dom Casmurro, que possui 148 capítulos, por isso, escolha um capítulo inserido no intervalo de 1 a 148. 

* Para receber o livro como audiobook:

    * Para o programa funcionar é necessário que previamente um grupo no Whatsapp seja criado com exatamente o nome "Dom Casmurro - Machado A." e neste grupo deve ser colocado o MP3 que pode ser encontrado <a href = "https://github.com/LissandraRodrigues/projeto_liv_mega_hack/blob/master/Dom_Casmurro_parte_1.mp3" > aqui. </a> 

    * python enviaAudio.py -n <Nome do usuário que você enviará o livro (tem que ser exatamente igual ao que está no WhatsApp)>
    
        Exemplo: python enviaMensagemTexto.py -n João

# Time

* <a href = "https://www.linkedin.com/in/luiza-lissandra/"> Luiza Lissandra </a> - Graduanda de Engenharia Eletrônica e de Computação na UFRJ.

* <a href = "https://www.linkedin.com/in/isabelazamith/"> Isabela Zamith </a> - Graduanda de Design de Mídia Digital na PUC-Rio.

* <a href = "https://www.linkedin.com/in/iurilopesalmeida/"> Iuri Almeida </a> - Graduando de Engenharia Agrícola e Ambiental na UFF.

* <a href = "https://www.linkedin.com/in/romulo-rizo-cabral/"> Rômulo Cabral </a> - Graduando de Engenharia de Computação na UERJ.

* <a href = "https://www.linkedin.com/in/luiz-cruz-bb2746162/"> Luiz Felipe </a> - Graduando de Engenharia de Automação e Controle na UFRJ.




