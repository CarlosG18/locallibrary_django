# parte 3 - usando o model

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
