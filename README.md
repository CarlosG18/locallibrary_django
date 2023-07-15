# locallibrary_django
Fazendo o exemplo do MDN Web Docs: Django Tutorial: [The Local Library website](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Tutorial_local_library_website)

## parte 1 - Entendendo o LocalLibrary

Neste exemplo o `LocalLibray` será um site com catálogo de livros, ao qual o usuário irá poder encontrar livros disponíveis, além de gerenciar sua conta.

## parte 2 - criando o esqueleto do site

- o arquivo `__init__.py` geralmente em branco é usado para tratar um diretório como um pacote.

- no arquivo de configuração de seu projeto `settings.py` existe o `DEBUG`. é recomendado que na produção essa variável seja atribuida como *false*, pois ela em *true* facilita na depuração, porém da brechas a invasões. portanto, durante  desenvolvimento dos códigos ela pode esta ativa.

**trocando a url raiz**: para trocar a url raiz use a RedirectView de uma generic view no arquivo `urls.py` do seu projeto. exemplo

```python 
from django.views.generic import RedirectView

urlpatterns = [
  path('', RedirectView.as_view(url='catalog/')),
]
```

- você pode habilitar a veiculação de arquivos estáticos durante o desenvolvimento:

```python 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```
A função `static()` é usada para adicionar as URLs necessárias para servir os arquivos estáticos da aplicação. Ela recebe dois argumentos: `settings.STATIC_URL` e `settings.STATIC_ROOT`, que são usados para construir as URLs corretas. Em outras palavras, quando uma solicitação é feita a uma URL que começa com `STATIC_URL`, o servidor web retorna o arquivo correspondente em `STATIC_ROOT`.

A configuração `settings.STATIC_URL` é a URL base na qual todos os arquivos estáticos da aplicação serão servidos. Por exemplo, se o valor de `STATIC_URL` for **'/static/'**, e um arquivo de folha de estilo for armazenado em **BASE_DIR / static / css / style.css**, o caminho completo para esse arquivo seria `http://example.com/static/css/style.css`

`settings.STATIC_ROOT` é o caminho absoluto para o diretório que contém todos os arquivos estáticos coletados com o comando `collectstatic`. Esse diretório é o local no qual o servidor web procura os arquivos estáticos para servir.

- toda vez que o models for modificado realize os seguintes comandos abaixo:

```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

## links para resumo das partes desenvolvidas:

- [parte 3 - usando o model](https://github.com/CarlosG18/locallibrary_django/tree/main/content/models.md)

- [parte 4: Django Admin Site](https://github.com/CarlosG18/locallibrary_django/tree/main/content/admin_site.md)

- [Parte 6: Lista Genérica e detail view](https://github.com/CarlosG18/locallibrary_django/tree/main/content/classviews.md)

- [parte 7 - Sessôes](https://github.com/CarlosG18/locallibrary_django/tree/main/content/session.md)

- [parte 8 - Autentificação de usuário e permissões](https://github.com/CarlosG18/locallibrary_django/tree/main/content/autentificacao.md)

- [parte 9 - trabalhando com forms](https://github.com/CarlosG18/locallibrary_django/tree/main/content/forms.md)

- [parte 10 - testes unitários](https://github.com/CarlosG18/locallibrary_django/tree/main/content/testes.md)

- - [parte 11 - deploy](https://github.com/CarlosG18/locallibrary_django/tree/main/content/deploy.md)


