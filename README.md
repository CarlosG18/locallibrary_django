# locallibrary_django
Fazendo o exemplo do MDN Web Docs: Django Tutorial: The Local Library website

## parte 1 - Entendendo o LocalLibrary

Neste exemplo o `LocalLibray` será um site com catálogo de livros, ao qual o usuário irá poder encontrar livros disponíveis, além de gerenciar sua conta.

## parte 2 - criando o esqueleto do site

- o arquivo `__init__.py` geralmente em branco é usado para tratar um diretório como um pacote.

- a pasta `migrations` possui arquivos que são responsáveis por fazer atualizações automáticas no banco de dados quando o models for alterado.

- no arquivo de configuração de seu projeto `settings.py` existe o `DEBUG`. é recomendado que na produção essa variável seja atribuida como *false*, pois ela em *true* facilita na depuração, porém da brechas a invasões. portanto, durante  desenvolvimento dos códigos ela pode esta ativa.

*trocando a url raiz*: 
