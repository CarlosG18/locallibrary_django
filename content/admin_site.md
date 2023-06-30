# parte 4: Django Admin Site

### registrando modelos

para registrar os seus modelos no site de admin, basta importar todos os seus modelos e usar o codigo abaixo:

```python
adimin.site.register(Modelo)
```

- para criar um superusuario:
```bash
$ python manage.py createsuperuser
```

### Configuração Avançada

alterando como o modelo é exibido no site de administração. para isso algumas etapas devem ser seguidas.

#### Adicionando class adminModel

- use o decorator `@admin.register(nome_do_model)`.
- crie uma classe seguindo o exemplo abaixo:
```python 
class nome_do_modelAdmin(admin.ModelAdmin):
  pass
```
usando a tupla `list_display` você modifica como o registro do seu model será visualizado no site de administraçao, pois seguindo o padrão o registro mostrará o retorno da funçao `__str__()` do seu model. neste list_display você colocará alguns ou todos os campos do seu model, e no site de administração cada registro será mostrado conforme a ordem dos campos informados no `list_display`.

#### Adicionando listas de filtros

para criar um filtro em seu site de administração use o `list_filter` seguindo a mesma ideia do `list_display`. isso criará uma caixa de filtro com os campos definidos no `list_filter`.

#### alterar a ordem dos campos

se você quiser alterar a ordem de como os campos devem ser apresentados use o `fields` em sua classe `nome_do_model_Admin`. um exemplo deste uso:
```python
fields = [('first_name','last_name'), 'born_date', 'nacionalidade']
```
neste exemplo, no site de administração irá mostrar os campos first_name e last_name em conjunto e os campos de born_date e nacionalidade serao mostrados separados.

#### Adicionado seções 

para adicionar seções no registro use o `fieldsets`. use da seguinte forma:
```python 
fieldsets = (
  ('nome_da_seção' {
    'fields': ('nome_do_campo','nome_do_campo')
  }),
  ('nome_da_seção1' {
    'fields': ('nome_do_campo','nome_do_campo')
  }),
)
```