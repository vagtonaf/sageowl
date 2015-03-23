Instalação do ambiente de trabalho:  ##Melhorar esse texto##

Com um grande potêncial a parceria Eclipse e Python promete um grande sucesso, começando com o Eclipse que tem grande número de plugins disponíveis, para trabalhar com a linguagem Python e utilizando o plugin Pydev, se mostra muito versátil. Como instalar esse plugin de forma bem prática e muito fácil?. Vamos ver logo abaixo:

Começamos com o Eclipse:
É preciso que você esteja com seu Eclipse previamente instalado, eu recomendo utilizar a versão 3.4.0, é a que estou usando para o desenvolvimento, ela é compatível com a última versão do Python, Pydev e Django.

Para que o Plugin para o Eclipse para a plataforma Python é o Pydev.

Podemos encontrar as plataformas acima nos links descritos abaixo:
http://www.djangoproject.com/
Home page oficial do Python: http://www.python.org.br/wiki
> Primeiramente vamos instalar o python:
Está Instalação é referecia para a utilização da linguagem python versão 2.6:  http://www.python.org/ftp/python/2.6.2/python-2.6.2.msi

Precisamos instalar o FrameWork Django no Python para que possa nos auxiliar na construção dos sites mais rapidamente:
(Python 2.6.x): http://media.djangobrasil.org/djangobrasil/downloads/Django-1.0_final.win32.py26.exe

Instalação do plugin do MySql no Python para que o python possa se conectar ao repositorio de dados que vamos utilizar nesse projeto, existem inumeros plugins para diversos bancos de dados existentes no mercado, como o Sql Server e Oracle
http://www.technicalbard.com/files/MySQL-python-1.2.2.win32-py2.6.exe

Utilizaremos nesse projeto um sistema de controle de versão desenhado especificamente para ser um substituto moderno do CVS, que se considera ter algumas limitações.
http://pt.wikipedia.org/wiki/Subversion
Instalação do SVN Repositorio
http://subclipse.tigris.org/install.html foi usado essa url para a instalação http://subclipse.tigris.org/update_1.6.x instalar no eclipse criar new repository location referenciar a url https://sageowl.googlecode.com/svn/trunk/ para direcionar o SVN para o projeto no Google Code, onde escolhemos para abrigar a aplicação.

para o seu login no gmail a senha e conseguida via esse link: http://code.google.com/hosting/settings
utilizaremos o command do prompt (cmd) do Windows, escolhemos essa plataforma de sistema operacional para o desenvolvimento.

O Django (tem que descompactar e executar o setup pelo cmd) MysqlDb? para conectar o python ao mysql
http://www.djangoproject.com/download/1.0.2/tarball/

e faz a fast install do pydev no seu eclipse como vemos no link: http://pydev.sourceforge.net/download.html

O Python já possui um recurso incorporado de um servidor web para testes, não é necessário instalar no momento do desenvolvimento da aplicação um servidor web, como o apache.

Pronto ai voce ja vai ter tudo que precisa para trabalhar com python (não precisa de mais nada).

E instala o plugin do pydev no seu eclipse, para não ter que ficar mechendo no notepad.

http://pydev.sourceforge.net/download.html

http://sourceforge.net/projects/pydev/files/

Poe o Python.exe no path e executa isso para criar um projeto:

python django-admin.py startproject meusite

ele vai criar um diretorio com os arquivos basicos do projeto, edita o arquivo settings.py e poe os dados do teu mysql; usuario, senha, etc... Entra no command e da CD no diretorio do projeto (onde tem um arquivo manager.py) e executa esse comando para iniciar o servidor:

python manage.py runserver

ai é só acessar pelo IE ou firefox http://127.0.0.1:8000/

pronto.


### ver referências de telas de instalação no link: http://www.plugmasters.com.br/sys/materias/716/1/Python-no-Eclipse-com-o-Pydev ####

paços da instalação do Python no Eclipse com o Pydev:
1) No Eclipse, selecione o menu help -> softwares updates -> find and install
2) Selecione Search for new features to install e clique em next
3) Na próxima tela clique no botão New Remote Site e preencha de acordo com a figura abaixo (Name: Pydev, URL: http://pydev.sourceforge.net/updates/)
4) Feito isso selecione apenas o Pydev e clique em finish
5) Selecione apenas o Pydev e clique em Next
6) Aceite a licença e clique em Next
7) Clique em finish para confirmar a instalação do plugin
8) O Eclipse vai fazer o download dos arquivos necessários para instalação do Pydev
9) Ao final do download a seguinte tela vai ser exibida, confirme com Install All
10) Depois de instalado ele vai pedir para reiniciar o Eclipse, confirme a operação
11) Selecione o menu Window -> Preference
12) Selecione Interpreter - Python e clique no botão New da configuração de Python interpreters
13) Selecione a localização do interpretador Python que está instalado em sua máquina, como eu estou utilizando o Windows eu apontarei para c:\python26. No Windows basta encontrar o executável python.exe (geralmente ele fica em C:\Python26). Depois de selecionar o interpretador a seguinte tela será exibida, confirme a seleção sem alterações
14) Mais um vez confirme clicando no botão Ok
15) O Pydev já está pronto para ser utilizado, crie um novo projeto selecionando o menu New -> Pydev Project
16) Preencha as opções conforme a figura abaixo e clique em finish
17) Já com seu projeto aberto, selecione a pasta src e crie um novo arquivo
18) Escolhe teste.py para o nome do seu novo arquivo e clique em finish
19) Agora você pode programar em Python utilizando o Eclipse, veja um exemplo do recurso de autocompletar utilizando um "import do datetime" é ele irá responder ao rodar que tem 0 erros, isso informa que está tudo funcionando corretamente.

Fonte de pesquisa: Trabalho Python no Eclipse com o Pydev - Allisson Azevedo trabalha com informática há 6 anos, atua nas áreas de gerenciamento de redes e desenvolvimento web.
consulta em 20/08/2009 as 0:44hs

Links relacionados
http://pydev.sourceforge.net/
http://www.eclipse.org/
http://www.python.org/