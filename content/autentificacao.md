# parte 8 - Autentificação de usuário e permissões

### criando usuários e grupos

**obs: os grupos e usuarios foram criados no site de admin**

- adicione a seguinte url no seu projeto:

```python
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
```

apos adicionar esta url, você terá acesso aos seguintes link porem sem templates:

- accounts/ login/ [name='login']
- accounts/ logout/ [name='logout']
- accounts/ password_change/ [name='password_change']
- accounts/ password_change/done/[name='password_change_done']
- accounts/ password_reset/ [name='password_reset']
- accounts/ password_reset/done/ [name='password_reset_done']
- accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
- accounts/ reset/done/ [name='password_reset_complete']

para informar os templates você devera usar a seguinte estrutura:

- crie uma pasta no seu diretorio de tamplates chamada `registration`;

os seguintes templates são os respetivos a:

- **login.html**: tela de login;
- **logged_out.html**: tela de logout;
- **password_reset_form.html**: tela de redefinição de senha;
- **password_reset_done.html**: tela de redefinição de senha comcluida;
- **password_reset_email.html**: tela de email de redefinição de senha;
- **password_reset_confirm.html**: tela de confirmação de redefinição de senha;
- **password_reset_complete.html**: tela de redefinição de senha concluida;

quando o usuario faz o login ele é direcionado para a url `localhost:8000/accounts/profile/` para mudar isso vá até o arquivo `settings` de seu projeto e faça:

```python
LOGIN_REDIRECT_URL = '/'
```
use o `{{ user.is_authenticated }}` para verificar se o usuario atual esta autenticado.

em uma url podemos usar variaveis adicionais como por exemplo:
```python
 <li><a href="{% url 'login' %}?next={{ request.path }}">Login</a></li>
```
neste caso usamos o `??next={{ request.path }}` que envia como parametro `next` para a view a url como conteudo, neste caso em particular, ao ser realizado o login ou logout a view que em que foi clicado (login/logout) voltará. isso pode ser usado pra enviar variaveis auxiliares.

- usando o decorator `@login_required` é possivel restringir o acesso em determinada function view. para importar use:

```python 
from django.contrib.auth.decorators import login_required
```
- para views baseadas em classes:

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class Minhaview(LoginRequiredMixin, View):
```
em query's podemos usar quantos `.filter` quisermos.

#### Permissões 

são as permissoes que os usuarios possuem para modificar os models no site de administração. a definição de permissões é realizada no model a partir da `class Meta`, usando o campo `permissions`. essas permissões são escritas em tuplas onde possui o nome da permisao e o valor de exibição da permissão.

as permissoes do usuario atual são guardadas em `{{ perms }}`. podemos usa-la para verificar se o usuario possui alguma permissão. nas views para testar uma permissão podemos usar o decorator `@permission_required("nome_da_permissão")` para views baseadas em função ou extender a classe `PermissionRequeridMixin` para views baseadas em classes, usando o `permission_required = 'nome_da_permissao'`

**obs:**
> @permission_required redireciona para a tela de login (HTTP Status 302). PermissionRequiredMixinretorna 403 (status HTTP proibido).