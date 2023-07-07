# trabalhando com Forms em django

## processo de manipulação de formulário Django

usamos o class `Form` para trabalhar com forms

alguns tipos de dados que podem ser usados em um form:
- BooleanField
- CharField
- ChoiceField
- TypedChoiceField
- DateField
- DateTimeField
- DecimalField
- DurationField
- EmailField
- FileField
- FilePathField
- FloatField
- ImageField
- IntegerField
- GenericIPAddressField
- MultipleChoiceField
- TypedMultipleChoiceField
- NullBooleanField
- RegexField
- SlugField
- TimeField
- URLField
- UUIDField
- ComboField
- MultiValueField
- SplitDateTimeField
- ModelMultipleChoiceField
- ModelChoiceField

alguns argumentos comuns:

- **required**: Se True, o campo não pode ficar em branco ou receber um Nonevalor. Os campos são obrigatórios por padrão, portanto, você deve definir required=Falsepara permitir valores em branco no formulário.

- **label**: o rótulo a ser usado ao renderizar o campo em HTML. Se um rótulo não for especificado, o Django criará um a partir do nome do campo colocando a primeira letra em maiúscula e substituindo sublinhados por espaços (por exemplo, data de renovação ).

- **label_suffix**: Por padrão, dois pontos são exibidos após o rótulo (por exemplo, Data de renovação​ : ). Este argumento permite que você especifique um sufixo diferente contendo outro(s) caractere(s).

- **initial**: O valor inicial do campo quando o formulário é exibido.

- **widget**: O widget de exibição a ser usado.

- **help_text**: Texto adicional que pode ser exibido em formulários para explicar como usar o campo.

- **error_messages**: uma lista de mensagens de erro para o campo. Você pode substituí-los por suas próprias mensagens, se necessário.

- **validators**: Uma lista de funções que serão chamadas no campo quando ele for validado.

- **localize**: Habilita a localização da entrada de dados do formulário.

- **disabled**: O campo é exibido, mas seu valor não pode ser editado se for True. O padrão é False.

## Validação

para acessar um dado em um form podemos usar o metodo `cleaned_data['nome_do_campo']`.

para levatarmos possiveis erros na validação dos dados inseridos no form podemos fazer uma limpagem nos dados alterando a função `def clean_nome_do_campo`:

```python
from django.core.exceptions import ValidationError

def clean_nome_do_campo(self):
    data = self.cleaned_data['nome_do_campo']

    #alguma regra para limpagem dos dados:
    #lance a exceção:
    raise ValidationError('message_error')
```

o django tambem oferece funções de tradução. para usa-las basta importar:

```python
from django.utils.translation import gettext_lazy as _
```

o que estiver em `_()` será traduzido de acordo com o idioma da pagina.

## etapas de uma view de um forms

1. primeiro, nos temos que redenrizar um form padrão para o usuario se for detectado um "primeiro" acesso e se esses dados forem para realizar atualizações no banco de dados (usando o metodo POST). para isso podemos fazer a seguinte verificação na view:

```python
    if request.method == "POST":
        #codigo
    else: # seria o equivalente ao GET
        form = Form()
    
    return render(request, "template", {
        'form': form, 
    })
```

ao usar o `form.is_valid()` ele irá verificar se todos os campos do formulario são validos, esse metodo tambem verifica funções internas do forms que são destinadas a limpagem de dados.

no template devemos usar o `{% csrf_token %}` para gerar uma criptografia para que os dados sejam enviados com segurança. 

