CAA e Bloom

http://www.economicsnetwork.ac.uk/handbook/printable/caa_v5.pdf

http://www.nwlink.com/~Donclark/hrd/bloom.html

http://download.intel.com/education/Common/br/Resources/DEP/skills/Bloom.pdf

http://74.125.47.132/search?q=cache:-NLeXIilkhMJ:www.cinted.ufrgs.br/ciclo9/artigos/12aLuizFernando.pdf+Se+o+trabalho+de+Raabe&cd=9&hl=pt-BR&ct=clnk&gl=br

http://lousadigital.blogspot.com/2008/11/taxonomia-de-bloom.html

SNV

http://www.djangoproject.com/

http://pt.wikipedia.org/wiki/Subversion

http://www.python.org.br/wiki

Instala o python 2.6

http://www.python.org/ftp/python/2.6.2/python-2.6.2.msi

(Python 2.6.x) http://media.djangobrasil.org/djangobrasil/downloads/Django-1.0_final.win32.py26.exe


O Django (tem que descompactar e executar o setup pelo cmd)

http://www.djangoproject.com/download/1.0.2/tarball/

MysqlDb para conectar o python ao mysql

http://www.technicalbard.com/files/MySQL-python-1.2.2.win32-py2.6.exe

e faz a fast install do pydev no seu eclipse

http://pydev.sourceforge.net/download.html

Não tem que instalar nada no apache.

MysqlDb para conectar o python ao mysql, e só dar 2 clicks depois next, next finish.

http://www.technicalbard.com/files/MySQL-python-1.2.2.win32-py2.6.exe

Pronto ai voce ja vai ter tudo que precisa para trabalhar com python (não precisa de mais nada).


E instala o plugin do pydev no seu eclipse, para não ter que ficar mechendo no notepad.


http://pydev.sourceforge.net/download.html

http://sourceforge.net/projects/pydev/files/

Poe o Python.exe no path e executa isso para criar um projeto :

python django-admin.py startproject meusite

ele vai criar um diretorio com os arquivos basicos do projeto, edita o arquivo settings.py e poe os dados do teu mysql; usuario, senha, etc...

Entra no command e da CD no diretorio do projeto (onde tem um arquivo manager.py) e executa esse comando para iniciar o servidor:

python manage.py runserver

ai é só acessar pelo IE ou firefox http://127.0.0.1:8000/

pronto.


http://blogdodantas.dxs.com.br/2009/02/19/instalando-mod_python-no-apache-python-e-web/
http://www.modpython.org/live/current/doc-html/inst-prerequisites.html

http://www.helder.eti.br/2009/06/pydev-com-django-no-ubuntu-904.html

Faz o download desse cara e poe no pendrive

Portable Python 1.1 based on Python 2.6.1


http://www.portablepython.com/releases/

Ele já vem com o django instalado.

Instalação do SVN Repositorio
> http://subclipse.tigris.org/install.html
> usar essa url
> http://subclipse.tigris.org/update_1.6.x
> instalar no eclipse
> criar new repository location
> referenciar a url https://sageowl.googlecode.com/svn/trunk/

> para o seu login no gmail
> a senha e conseguida via esse link: http://code.google.com/hosting/settings

Graficos

biblioteca Grafica e matematica
Numpy:
http://sourceforge.net/projects/numpy/files/NumPy/1.3.0rc2/numpy-1.3.0rc2-win32-superpack-python2.6.exe/download

http://sourceforge.net/projects/scipy/files/scipy/0.7.1/scipy-0.7.1-win32-superpack-python2.6.exe/download

http://en.sourceforge.jp/projects/sfnet_scipy/downloads/scipy/0.7.1/scipy-0.7.1-win32-superpack-python2.6.exe/
ver arquivo exemplo no wiki download: grafico.py

##### servidor ########


> Por onde começar para instalar um servidor
> Python / Django

Acredito que o site aprendendo django do Marinho seja de grande
utilidade. Para instalar no seu ambiente de desenvolvimento, leia:
Capítulo 3: Baixando e Instalando o Django [1](1.md).

Para instalar em um servidor Windows, recomendo a leitura do Cáp. 16
[2](2.md). Sobre deploy [3](3.md).

> Como devemos configurar e o que deve instalar para
> conviver, se possível as duas aplicações Django e Web2py?

Depois que tiver o ambiente em Django funcional, recomendo que visite
o site do web2py [4](4.md) e visite a seção de "Downloads" e
"Documentation". A versão do web2py para windows vem com um auto-
executável similar ao Wamp e outros.

[1](1.md) http://www.aprendendodjango.com/baixando-e-instalando-o-django/
[2](2.md) http://www.aprendendodjango.com/preparando-um-servidor-com-windows/
[3](3.md) http://www.aprendendodjango.com/infinitas-formas-de-se-fazer-deploy/
[4](4.md) http://web2py.com/

############################################

Instale primeiro o Apache. Instalador normal mesmo (NNF - Next, Next, Finish). Depois instale o Python. Depois o Banco de dados. Depois o Django. Depois o módulo MySQLDB e o mod\_wsgi (que é só fazer referência no apache). Instale o Web2Py. No restante é só configurar as aplicações. Se quiser dar uma melhorada no desempenho, dá pra configurar o apache, mantendo 2 instâncias dele, uma escutando em cada porta. Em uma delas você aumenta o cache, e utiliza para publicação de arquivos estáticos. Fica até razoável.