# VAAlugar-MS-avaliacoes
Repositório do projeto VA'Alugar em Microsserviços (MS) para a gestão das avaliações. Para mais informações sobre este projeto, consultar o readme do repositório Gateway: https://github.com/fabioFernandesBR/VAAlugar-MS-gateway/blob/main/README.md.

As funcionalidades disponíveis são Postagem de Avalição, na rota /criar, e Exclusão de Avaliação, na rota /excluir, e Consulta, na rota /graphql. As duas primeiras estão disponíveis como chamadas REST.


## ATENÇÃO: RODA NA PORTA 5004.


## Esquema de Fluxo de informações:
Disponibiliza as seguintes rota para comunicação via REST:

### /criar
Passar um dicionário com o seguinte padrão:
{
  "comentario": "string" (Optional),
  "id_reserva": int,
  "id_canoa": int,
  "id_usuario": "string",
  "nota": float
}

Exemplo:
{
  "comentario": "Muito bom",
  "id_reserva": 25,
  "id_canoa": 8,
  "id_usuario": "21999999999",
  "nota": 7.5
}

Retorna:
{
  "comentario": "Muito bom",
  "id_avaliacao": 50,
  "id_canoa": 8,
  "id_usuario": "21999999999",
  "nota": 7.5,
  "nova_media": 6.5,
  "nova_quantidade": 14
}


### /excluir
Passar um dicionário com o seguinte padrão:
{
  "id_avaliacao": int
}

Exemplo:
{
  "id_avaliacao": 30
}

Retorna:
{
  "comentario": "Excelente!",
  "id_avaliacao": 30,
  "id_canoa": 5,
  "id_usuario": "21999999999",
  "nota": 10,
  "nova_media": 9,
  "nova_quantidade": 12
}

### Consulta via graphql
Com a rota /graphql, diferentes parâmetros podem ser passados via GraphQL, para consulta das postagens:
- query se chama posts.
- 3 critérios de busca são habilitados: idCanoa, idUsuario e idReserva.
- idCanoa e idReserva são passados como int, enquanto idUsuario é passado como string.
- As consultas podem ser feitas por 1, 2, todos ou nenhum dos critérios. Observe porém que idPost é chave primária, ou seja, se você souber qual é o idPost que você está buscando, não é necessário passar nenhum outro parâmetro.
- pode-se especificar os campos necessários no retorno.

Exemplos:
{query: posts{
  idCanoa
  idUsuario
  nota
  comentario
  idReserva
  idPost
}} retorna todas as postagens.

{query: posts{
  nota
  comentario
}} retorna apenas nota e comentário de todas as postagens.

{query: posts (idUsuario: "21994497882"){
  idCanoa
  idUsuario
  nota
  comentario
  idReserva
  idPost
}} 

retorna todas as postagens feitas pelo usuário "21994497882": {
  "data": {
    "query": [
      {
        "idCanoa": 9,
        "idUsuario": "21994497882",
        "nota": 10,
        "comentario": "Legal demais",
        "idReserva": 11,
        "idPost": 16
      },
      {
        "idCanoa": 6,
        "idUsuario": "21994497882",
        "nota": 7.8,
        "comentario": "Bacana",
        "idReserva": 12,
        "idPost": 17
      }
    ]
  }
}

enquanto:

{query: posts (idUsuario: "21994497882", idCanoa: 6){
  nota
  comentario
}}
retorna apenas nota e comentário da única postagem realizada pelo usuario "21994497882" a respeito da canoa 6: {
  "data": {
    "query": [
      {
        "idCanoa": 6,
        "idUsuario": "21994497882",
        "nota": 7.8,
        "comentario": "Bacana",
        "idReserva": 12,
        "idPost": 17
      }
    ]
  }
}.

{query: posts (idUsuario: "21999999999", idCanoa: 1){
  nota
  comentario
  idReserva
}} retorna as notas, comentários e idReservas de todas as postagens realizadas pelo usuário "21999999999" a respeito da canoa 1:

{
  "data": {
    "query": [
      {
        "nota": 5,
        "comentario": "Totalmente Excelente!!",
        "idReserva": 5
      },
      {
        "nota": 9,
        "comentario": "legal",
        "idReserva": 7
      },
      {
        "nota": 5,
        "comentario": "Totalmente Excelente!!",
        "idReserva": 4
      },
      {
        "nota": 10,
        "comentario": "supercool 3",
        "idReserva": 1
      },
      {
        "nota": 10,
        "comentario": "supercool 2",
        "idReserva": 2
      },
      {
        "nota": 10,
        "comentario": "supercool 2",
        "idReserva": 3
      },
      {
        "nota": 10,
        "comentario": "quase lá",
        "idReserva": 6
      }
    ]
  }
}

finalmente:

{query: posts (idReserva: 18) {
  idCanoa
  idUsuario
  nota
  comentario
  idReserva
  idPost
} }

retorna todas as informações relacionadas à postagem 18:

{
  "data": {
    "query": [
      {
        "idCanoa": 4,
        "idUsuario": "21984561237",
        "nota": 10,
        "comentario": "Muito legal!",
        "idReserva": 18,
        "idPost": 21
      }
    ]
  }
}



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
Considere as seguintes opções: instalar apenas este microsserviço, diretamente do IDE, como Visual Studio Code; ou instalar todos os microsserviços via Docker Compose.

### Para rodar este MS diretamente do IDE.
No Windows:
1. Faça o clone deste repositório para sua máquina.
2. Crie um ambiente virtual, com o comando "Python -m venv env", diretamente no terminal.
3. Em seguida ative o ambiente virtual, com o comando ".\env\Scripts\activate".
4. Instale as dependências necessárias com o comando "pip install -r requirements.txt".
5. Execute com o comando "flask run --host 0.0.0.0 --port 5002"
Para Mac ou Linux, a lógica é a mesma, mas faça as adaptações necessárias.

### Como executar através do Docker Compose
Para que os microsserviços interajam, é necessário que todos estejam rodando. A forma mais fácil de instalar e executar todos está descrita no link:
https://github.com/fabioFernandesBR/VAAlugar-Docker-Compose/blob/main/README.md
