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

- **help_text(como visto no exemplo acima)**: Texto adicional que pode ser exibido em formulários para explicar como usar o campo.

- **error_messages**: uma lista de mensagens de erro para o campo. Você pode substituí-los por suas próprias mensagens, se necessário.

- **validators**: Uma lista de funções que serão chamadas no campo quando ele for validado.

- **localize**: Habilita a localização da entrada de dados do formulário (veja o link para mais informações).

- **disabled**: O campo é exibido, mas seu valor não pode ser editado se for True. O padrão é False.
