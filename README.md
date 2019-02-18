# API-RESTful-Gerenciador-de-Contatos-Python-Django-
API construida em Python/Django para gerenciar uma lista de contatos. O objetivo desse projeto é fazer uma API RESTfull usando o Django, que permita visualizar uma lista de contatos, além de criar, remover e atualizar as informações do contato. O projeto foi desenvolvido numa metodologia orientada a teste e o módulo de testes do django (TestCase) foi a ferramenta escolhida para os testes automatizados.

## Instalação

Essa aplicação usando o Conda como ambiente e utiliza as bibliotecas do Django e do Projeto Anaconda. Para uma melhor integração recomendo a instalação do Anacoda 3 ou mais recente. Esse programa é baseado em python 3.7 e utiliza as bibliotecas: Django, json e requests.

Para rodar o programa basta baixar os arquivos do projeto e, na pasta dos arquivos, rodar:

```
python manage.py runserver

```

Dessa maneira a aplicação estará disponível e você poderá acessa-la através do local host http://127.0.0.1:8000/.

## Funcionalidades

Assim que acessamos a aplicação pelo browser podemos ver:

![Tela inicial](https://github.com/Lucas-Armand/API-RESTful-Gerenciador-de-Contatos-Python-Django-/blob/master/img/tela%20aplicacao1.png)

Nessa exibição é possível ver os dados json dos dez primeiros contatos da lista de contatos. É possível perceber, na barra de url, que a aplicação redirecionou o acesso para introduzir os filtros de busca de resultados. Na imagem a seguir podemos ver que alterando os valores passador pelo requerimento é possível ter uma seleção arbitraria de contatos sequencias:

![Seleção arbitrária de contatos](https://github.com/Lucas-Armand/API-RESTful-Gerenciador-de-Contatos-Python-Django-/blob/master/img/tela%20aplicacao%202.png)

Também pode ser interessante acessar individualmente algum contato. A imagem a seguir apresenta o exemplo do acesso do contato número um, mas qualquer contato pode ser acessado por sua posição no banco de dados:

![Seleção arbitrária de contatos](https://github.com/Lucas-Armand/API-RESTful-Gerenciador-de-Contatos-Python-Django-/blob/master/img/tela%20aplicacao%203.png)

Além disso é possível criar novos contatos (POST), atualizar contatos já existentes (PUT) e apagar contatos obsoletos (DELETE). Para exemplificar isso temos o arquivo de testes automáticos:


![Seleção arbitrária de contatos](https://github.com/Lucas-Armand/API-RESTful-Gerenciador-de-Contatos-Python-Django-/blob/master/img/tela%20aplicacao%204.png)

Nele é possível ver todos os tipos de requisições sendo feitas. Além disso, os testes automáticos foram utilizados nesse projeto tanto como ferramenta da metodologia de desenvolvimento, como para garantir a manutenção de todas as funcionalidades ao longo do desenvolvimento:

![Seleção arbitrária de contatos](https://github.com/Lucas-Armand/API-RESTful-Gerenciador-de-Contatos-Python-Django-/blob/master/img/tela%20aplicacao%205.png)





