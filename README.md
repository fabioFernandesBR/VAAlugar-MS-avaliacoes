# VAAlugar-MS-avaliacoes

## ATENÇÃO: RODA NA PORTA 5004.



## Criação do banco de dados: 1 tabela!!
CREATE TABLE avaliacoes (
    id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_canoa     INTEGER NOT NULL,
    nota         FLOAT   NOT NULL,
    comentario   TEXT,
    id_usuario   TEXT    NOT NULL,
    id_reserva   INTEGER NOT NULL
                         UNIQUE
);


## Instalação
Para instalar: use o arquivo requirements.txt para instalar os módulos. No windows: pip install -r requirements.txt Recomendo instalação em um ambiente virtual

Para executar localmente, em ambiente Windows: flask run --host 0.0.0.0 --port 5004 --reload

## Como executar através do Docker
Como os diferentes APIs comunicam-se entre si, é necessário usar o Docker Compose. Por isso, seguir as instruções para construção do Docker-compose no link:
https://github.com/fabioFernandesBR/VAAlugar-Docker-Compose/blob/main/README.md
