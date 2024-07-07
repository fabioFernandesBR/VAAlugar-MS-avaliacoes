# VAAlugar-MS-avaliacoes

## ATENÇÃO: RODA NA PORTA 5003.



## Parâmetros






## Criação do banco de dados: 1 tabela!!
CREATE TABLE avaliacoes (
    id_avaliacao     INTEGER PRIMARY KEY AUTOINCREMENT,
    id_canoa         INTEGER,
    nota             FLOAT,
    comentario       TEXT,
    id_usuario       INTEGER
);

## Instalação
Para instalar: use o arquivo requirements.txt para instalar os módulos. No windows: pip install -r requirements.txt Recomendo instalação em um ambiente virtual

Para executar localmente, em ambiente Windows: flask run --host 0.0.0.0 --port 5000 --reload

## Como executar através do Docker
Certifique-se de ter o Docker instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal. Execute como administrador o seguinte comando para construir a imagem Docker:

docker build -t ms-avaliacoes .
Uma vez criada a imagem, para executar o container basta executar, como administrador, seguinte o comando:

docker run -p 5003:5003 ms-avaliacoes

Uma vez executando, para acessar a API, basta abrir o http://localhost:5003/ no navegador.
