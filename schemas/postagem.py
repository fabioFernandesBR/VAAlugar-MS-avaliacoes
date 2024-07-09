from pydantic import BaseModel
from typing import Optional



# BaseModel é a classe base do Pydantic.
# As classes a seguir são modelos de dados baseadas em Pydantic.


# Operações que queremos implementar:
## Criar um post de avaliação (nota + comentário)
## Excluir um post de avaliação

class SchemaPostagemAvaliacao(BaseModel):
    """ 
    Define como uma nova avaliação de uma canoa a ser postada deve ser representada. 
    Fluxo: do usuário para a API. 

    Método POST
    """
    id_reserva: int = 1
    id_canoa: int = 1
    id_usuario: str = "21999999999"
    nota: float = 5
    comentario: str = "Totalmente Excelente!!"

class SchemaExclusaoAvaliacao(BaseModel):
    """ 
    Define como uma postagem / avaliacao a ser excluída deve ser representada. 
    Fluxo: do usuário para a API. 

    Método DELETE
    """
    id_avaliacao: int


class SchemaVisualizacaoPostagem(BaseModel):
    """ 
    Define como uma nova postagem recém criada ou excluída deve ser representada. 
    Fluxo: da API para o usuário.
    """
    id_avaliacao: int = 1
    id_canoa: int
    id_usuario: str
    nota: float
    comentario: str = "Totalmente Excelente!"
    nova_quantidade: int
    nova_media: float
    


def comunica_avaliacao_completa(avaliacao, nova_quantidade, nova_media):

    
    """Retorna uma representação da avaliação."""
    return {
        "id_reserva": avaliacao.id_reserva,
        "id_canoa": avaliacao.id_canoa,
        "id_usuario": avaliacao.id_usuario,
        "nota": avaliacao.nota,
        "comentário": avaliacao.comentario,
        "nova media de avaliações": nova_media,
        "nova quantidade de avaliações": nova_quantidade,
    }
