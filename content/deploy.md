# Deploy

- [lista](https://djangofriendly.com/index.html) de provedores de hospedagem que trabalham com o django.

alguns serviços de produção:
- railway
- Python Anywhere
- Amazon Web Services
- Microsoft Azure
- Heroku
- Digital Ocean

## preparando seu site para publicação 
algumas configurações do seu arquivo `settings.py` de seu projeto devem ser alteradas:

- **DEBUG = FALSE**
- **SECRECT_KEY**

use o comando abaixo para fazer a checagem das alterações que devem ser feitas:

```shell
python3 manage.py check --deploy
```

## instalando o locallibrary no railway

alguns arquivos de texto são necessários:

- runtime.txt : informa a linguagem de programação e a versão a ser usada.
- requirements.txt : lista as dependências do Python necessárias para o seu site, incluindo Django.
- Procfile : Uma lista de processos a serem executados para iniciar o aplicativo da web. Para o Django, geralmente será o servidor de aplicativos web Gunicorn (com um .wsgiscript).
- wsgi.py : Configuração WSGI para chamar nossa aplicação Django no ambiente Railway.

### configurando o arquivo Procfile

cria-se um arquivo `Procfile` na raiz do diretório e adicionado esses comandos:

```txt
web: python manage.py migrate && python manage.py collectstatic && gunicorn locallibrary.wsgi
```

### configuração do banco de dados

`dj-database-url` é usado para extrair a configuração de um banco de dados django de uma variavel de ambiente.

### servindo arquivo estaticos

variaveis importantes:

- **STATIC_URL**: este é o local base do URL a partir do qual os arquivos estáticos serão exibidos, por exemplo, em um CDN.
- **STATIC_ROOT**: Este é o caminho absoluto para um diretório onde a ferramenta collectstatic do Django reunirá todos os arquivos estáticos referenciados em nossos modelos. Depois de coletados, eles podem ser enviados como um grupo para onde os arquivos serão hospedados.
- **STATICFILES_DIRS**: lista os diretórios adicionais que a ferramenta collectstatic do Django deve procurar por arquivos estáticos.

use o comando abaixo para coletar os arquivos estaticos na pasta `STATIC_ROOT`

```bash
python3 manage.py collectstatic
```

para os arquivos estaticos vamos usar o whitenoise.
