# Parte 6: Lista Genérica e detail view

no seu arquivo urls.py de sua aplicação use como por exemplo: `views.BookListView.as_view()` no argumento do path, ela possui um formato diferente porque agora ela a view vai ser definida como uma classe e não mas como função.

### View LIST (baseada em classe)

para usar as views genericas use a importação: `from django.views import generic`

crie a classe **BookListView** seguindo o exemplo anterior:
```python
class BookListView(generic.ListView):
  ...
```
**atributos da sub-classe:**
- model: modelo para a list view
- context_object_name: nome do contexto que será passado para o template
- queryset: consulta do banco que sera passado para o template
- template_name: caminho do template

#### substituindo métodos em class-based views

voce pode criar um metodo para adicionar variaveis de contexto adicionais.

observe o codigo abaixo:
```python
class BookListView(generic.ListView):
  model = Book

  def get_context_data(self, **kwargs):
    # obtenha o contexto atual
    context = super(BookListView, self).get_context_data(**kwargs)
    # adicione o contexto
    context['novo_contexto'] = 'novo contexto adicionado ao contexto orignal'
    return context
```

### View DETAIL (baseada em classe)

também existe uma generic view para detalhes do model. o que irá mudar é que a class `BookDetailView` herdará de `generic.DetailView`

#### passando opções adicionais em seus mapas de url

para realizar isso você deve usar um dicionario e coloca-lo no terceiro argumento da funcao `path`

podemos usar um shortcuts para verificar se o tal registro existe: `from django.shortcuts import get_object_or_404` essa função nos retorna o objeto caso ele exista ou um erro 404. isso para o caso de implementação de uma detail view com função.

uma forma de acessar os elementos que possuem algum relacionamento, como por exemplo o `ForeignKey`, podemos usar a função por exemplo **book.bookinstance_set.all()** para obter todos os registros que o book possui de bookinstance.

### Paginação

paginação esta embutido nas generics views usando o atributo `paginate_by` da classe. apartir do numero informado neste atributo a visualização começará a paginar os dados. usando os parametros `GET`. **exemplo: catalog/books?page=2**

- usamos o `{{ request.path }}` para obter a **URL** da pagina atual.
- `is_pagination` verifica se a pagina possui paginação;
- `page_obj` é o objeto de **Paginator**;
- `.has_previous` verifica se há pagina anterior;
- `.number` numero da página atual;
- `.paginator.num_pages` numero de páginas total;
- `.has_next` verifica se há proxima página
- `.next_page_number` retorna o número da proxima página
- `previous_page_number` retorna o número da página anterior
