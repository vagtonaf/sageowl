Após a intalação do Django, ao executar o comando de exemplo abaixo, criaremos o projeto com o nome "meuprojeto":
> djangoadmin.py startprojet meuprojeto
Obteremos como resultado quatro arquivos criados em uma pasta de arquivos que são descritos a seguir:

1) "init.py"  é um arquivo que mostra ao Python que está pasta de arquivos é considerada como um pacote. Ele é um arquivo vazio e ele é criado tanto projetos como aplicações que veremos logo a seguir.

2) "manage.py" permite com que o desenvolvedor interjá com o projeto de várias maneiras diferentes, atraves de um utilitário de linha de comando.

3) "settings.py" é onde se encontram as configurações e definições referentes ao projeto.

4) "urls.py" concentra as declarações das URLs do projeto, contém uma tabela de conteúdos dos sites utilizados pelo Django.

Criaremos agora uma aplicação de nome "contatos" com o seguinte comando:
> python manage.py startapp contatos
É importante observar que devemos executar o comando dentro da pasta do projeto para que ao ser executado ele crie uma pasta com o nome da aplicação contendo mais três arquivos que são o "ini.py" é os arquivos "models.py" e "views.py" que são respectivamente, primeiro o responsável pelos dados da aplicação e segundo o responsável pela interface da aplicação.

O Eclipse com o plug-in PyDev é uma das melhores IDEs para desenvolvimento, inclusive em Python. E oferece um bom suporte ao desenvolvimento com o django. Este artigo é baseado em posts de outros blogs e experiência pessoal do autor.

## Modificar ###
Instalação do Django

Existem várias formas para instalar o Django. A que eu mais gosto e recomendo é através do tarball. Para isso, vá ao site[3](3.md) do django e baixe o arquivo .tar.gz. Então descompacte no caminho desejado e execute:

Link de instalção http://media.djangobrasil.org/djangobrasil/downloads/Django-1.0_final.win32.py24.exe

$sudo python2.4 setup.py install

Recomendo fortemente a utilização do python2.4 com o django. Esta versão do interpretador não vem por padrão no Ubuntu 9.04.

Instalação o Eclipse+PyDev

Para instalar o Eclipse, se ainda não o fez, basta acessar o site[1](1.md), realizar o download do mesmo e descompactar no caminho desejado. Supondo que o JDK tenha sido previamente instalado, deverá funcionar.

A instalação do PyDev é ainda mais fácil. No Eclipse:

Acesse "Help > Software Updates";
Selecione a aba "Available Software" e clique em "Add Site";
Entre com o endereço http://pydev.sourceforge.net/updates/. O Eclipse exibirá a opção PyDev Update Site. Marque e clique "Install";
Aceite os termos de uso; Next, Next e Finish. O Eclipse fará o restante.
Configuração do PyDev


No Eclipse, faça:

Windows > Preferences;
Expanda a opção PyDev e selecione "Interpreter - Python";
Clique em "New" e informe o caminho para o interpretador /usr/bin/python2.4;
Clique em Ok, para salvar as configurações.
Criando um projeto Django


No Eclipse, clique em "File > New Project"; Selecione PyDev, PyDev Project e clique Next; Entre com o nome do projeto e Finish.

Abra o terminal e acesse o subdiretório src do projeto recém-criado e então execute:

$ django-admin startproject mysite

Onde mysite deverá ser substituído pelo nome de sua escolha.

De volta ao Eclipse, faça um "refresh" no projeto (File > Refresh, ou simplesmente F5 com o projeto selecionado). Os módulos gerados automaticamente pelo django deverão ser apresentados.

Abra o módulo manage.py
Run > Run Configurations...
Crie uma nova configuração, setando o projeto, o módulo principal apontando para "manage.py";
Na área de argumentos (Arguments), entre com runserver --noreload no campo "Program Arguments" e o caminho completo para a pasta mysite em "Working Directory";
Clique "Apply" e "Run".
Para acessar o site, abra o Firefox e acesse http://localhost:8000/.

Referências

Projeto Eclipse Foundation. Ottawa, Ontario, Canada. 2004. Disponível em: <http://www.eclipse.org>. Acesso em: 7, jul, 2009.

Pydev Open Source Project. Pydev Sponsors. Aptana. 2002. Disponível em: <http://pydev.sourceforge.net>. Acesso em: 9, jul, 2009.

Django Project open-source. BSD license. 2009. Disponível em: <http://www.djangoproject.com>. Acesso em 12, jul, 2009.

Framework Django Brasil Projeto Aberto. Grupo de discursão. Disponível em: <http://www.djangobrasil.org>. Acesso em 15, jul, 2009.

The Django Book. Copyright 2006, 2007, 2008, 2009 Adrian Holovaty and Jacob Kaplan-Moss.
Disponível em: <http://www.djangobook.com>. Acesso em 17, jul, 2009.

Django+PyDev on Feisty. 2007.  Disponível em: <http://solyaris.wordpress.com/2007/05/16/how-to-djangopydev-on-feisty>. Acesso em 17, jul, 2009.

Como usar o Eclipse para desenvolver em Python, especialmente Zope/Plone. Rafael Oliveira. Mestrado em Ciências da Informação. UFMG. 2009. Disponível em: <http://rafaelb.objectis.net>. Acesso em 18, jul, 2009.

O framework Django. Eduardo Steiner. PET Computação. UFSC. 2008. Disponível em: < http://pet.inf.ufsc.br/files/django.pdf >. Acesso em 18, jul, 2009.

Django, Aptana, Gimp, Inkscape. Rafael Campos de Bastiani. Caxias do Sul. RS. RFDev.org. 2008. Disponível em: <http://rfdev.org>. Acesso em 20, jul, 2009.