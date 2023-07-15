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