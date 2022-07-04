# Cadastro usuário WEB

![Shields](https://img.shields.io/pypi/djversions/djangorestframework)

## Para executar o projeto, siga os seguintes passos (Digite no terminal após clonar o repositorio).

1.Abrar o MySQL workbench e execute o comando: create database pontotel; e depois: use pontotel; Após executar esses dois comando no Workbench, acesse o arquivo settings.py do projeto e certifique-se de inserir seu usuário e senha do banco de dados para que o projeto consiga ter acesso ao mesmo.

2.Crie uma venv com o comando: python -m venv venv

3.Em seguida ative a venv com o comando: venv\Scripts\activate.bat

4.Após ativar o ambiente virtual, execute o seguinte comando: pip install requirements.txt

5.Depois de instalar as bibliotecas necessarias para o funcionamento do projeto, execute o comando: py manage.py makemigrations

6.Depois para por fim executar o projeto, execute o comando: py manage.py runserver 
(certifique-se do projeto está rodando na porta 8000)

## Sobre o projeto

Este projeto foi criado para o envio do desafio proposto pela empresa. Utilizando recursos da linguagem Python, juntamente com seu framework Django e do Django-Rest-Framework.

O objetivo do projeto foi tentar criar um backend que serviria como base para o projeto de cadastro de usuários,
e este objetivo foi apenas parcialmente satisfeito, porém, no desenvolvimento do projeto foram aplicada tecnicas
para manipular dados de entrada a partir uso de API Rest e endpoints, juntamente com as respectivas responses após 
concluida cada operação. Os models foram serializados utilizando o Rest Framework e partir dessa serialização as API's 
para o CRUD de usuários foram instanciadas e depois isso foi enviado para através dos endpoint(URL's) para que fossem
chamados no front a partir do Axios e fossem posteriormente utilizados.

## Tecnologias utilizadas 

- Python
- Django Framework
- Django Rest Framework
- MySQL (BD relacional)
- Drf spectacular (Para documentação das API's via Swagger)
