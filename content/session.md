# Sessões

### usando sessões
você pode acessar o atributo `session` na view apartir do parâmetro `request`. ele é um dicionario. exemplo:

```python
request.session['nome'] = 'carlos'
```

### obtendo a contagem de visitas do site

```python
num_visitas = request.session.get('num_visitas', 0)
request.session['num_visitas'] = num_visitas+1
```
explicando o codigo anterior, a primeira linha cria uma chave chamada `num_visitas` e seta 0 para ela caso ela ainda não foi criada.
já na segunda linha, a cada atualizada na home do site ele irá pegar a variavel de sessao `num_visitas` e incrementar.
