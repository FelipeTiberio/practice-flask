# Tutorial de flask

Comecei a estudar flask para desenvolver uma aplicação para uma das minhas disciplinas no curso de T.I. da UFRN, estou usando esse app para documentar cada passo, e para ir anotando qualquer coisa que achar interessante ou importante lembrar no futuro.

A minha intenção aqui não é criar um tutorial para ajudar outras pessoas, apenas um lugar para lembrar as coisas que fiz.

link para o tutorial original:

<https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>

## Estou usando o pipenv para como ambiente virtual e gerenciar pacotes e dependências

 pip3 install pipenv
 pipenv install

## Resumo Part 1

No commit com legenda 'Hello, World!', está a primeira parte do tutorial

 microblog/
  venv/
  app/
    __init__.py
    routes.py
  microblog.py

Criei um pacote app.
Em app utilizei uma instância de Flask para setar o nome do modulo.
Crei apanas uma rota em routes.py, que tem como resposta
apenas uma função com a string hello, world. E por último criei um
arquino python microblog.py onde ira funcinar o main module.