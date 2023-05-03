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

## parte 3 - usando o model

alguns tipos de relação entre os models:

*obs:* `1..*` é a quantidade minima e máxima respectivamente.

- **um para um(OneToOneField)** 
- **um para muitos(ForeignKey)**
- **muitos para muitos(ManyToManyField)** 

### campos (Fields):

é o relacionado a coluna da tabela. 

#### Tipos de Campos

- **CharField**: é usado para strings. use o max_length (tamanho máximo) para o dado que será armazenado.

- **IntegerField**: é usado para inteiros.
    
- **DateField e DateTimeField**: são usados para armazenar / representar datas e informações de data / hora (como os objetos Python datetime.date in e datetime.datetime, respectivamente)
    
- **EmailField**: é usada para armazenara e validar em endereço de email.

- **FileField e ImageField**: são usados para carregar arquivos e imagens respectivamente.
    
- **AutoField** é um tipo especial de IntegerField que é incrementada automaticamente.
    
- **ForeignKey**: é usado para especificar um relacionamento um-para-muitos (chave estrangeira).

- **ManyToManyField**: é usado para especificar um relacionamento muitos-para-muitos.

argumentos comuns de um campo:

#### Argumentos

- **help_text**: Fornece um rótulo de texto para formulários HTML.

- **verbose_name**: Um nome legível para o campo usado nos rótulos de campo. Se não for especificado, o Django irá inferir o nome detalhado do campo name.

- **default**: O valor padrão para o campo.
    
- **null**: Se for True, o Django armazenará valores em branco como NULL no banco de dados, para campos onde isso é apropriado. O padrão é False.
    
- **blank**:Se for True, o campo poderá ficar em branco nos seus formulários. O padrão é False, o que significa que a validação de formulário do Django forçará você a inserir um valor. Isso é frequentemente usado com null = True.

- **choices**: Um grupo de escolhas para este campo.

- **primary_key**:Se True, define o campo atual como a chave primária do modelo. Se nenhum campo for especificado como a chave primária, o Django adicionará automaticamente um campo para essa finalidade.

#### Metadados

função: controlar a ordem padrao dos registros retornados.

#### Métodos

use o metodo de classe padrao do python `__st__()` para retornar uma string legivel para o seu objeto.

- get_absolute_url:

```python 
from django.urls import reverse

def get_absolute_url(self):
    """Retorna o URL para acessar uma instância específica do modelo."""
    return reverse('model-detail-view', args=[str(self.id)])
```
#### procurando por registros 

exemplo:

```python
all_books = Book.objects.all()
love_books = Book.objects.filter(title__contains='love')
```

no filter podemos usar o seguinte formato: `nome_do_campo__match_type`, onde temos o match type como por exemplo:
- **contains**: correspondência de maiúsculas e minúsculas.

- **icontains**: insensitivo a maiúsculas e minúsculas

- **iexact**: correspondência exata que não diferencia maiúsculas e minúsculas, 

- **exata**: correspondência exata diferencia maiúsculas de minúsculas 

- **gt**: maior que;

para usar o filter com outros modelos:


```python
action_books = Book.objects.filter(genero__nome __icontains='action')
```
onde genero é outro model e nome é um campo de genero.

## parte 4: Django Admin Site

### registrando modelos

para registrar os seus modelos no site de admin, basta importar todos os seus modelos e usar o codigo abaixo:

```python
adimin.site.register(Modelo)
```

- para criar um superusuario:
```bash
$ python manage.py createsuperuser
```

