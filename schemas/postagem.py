from pydantic import BaseModel
from typing import Optional, List



# BaseModel é a classe base do Pydantic.
# As classes a seguir são modelos de dados baseadas em Pydantic.


# Operações que queremos implementar:
## Criar canoa
## Deletar canoa
## Consultar canoa, informando dados como lista de locais, dono ou tipo de canoa

class SchemaPostagemAvaliacao(BaseModel):
    """ 
    Define como uma nova avaliação de uma canoa a ser postada deve ser representada. 
    Fluxo: do usuário para a API. 

    Método POST
    """
    id_canoa: int = 1
    id_usuario: int = 21999999999
    nota: float = 5
    comentario: str = "Totalmente Excelente!!"

class SchemaExclusaoAvaliacao(BaseModel):
    """ 
    Define como uma postagem / avaliacao a ser excluída deve ser representada. 
    Fluxo: do usuário para a API. 

    Método DELETE
    """
    id_avaliacao: int


class SchemaAtualizacaoAvaliacao(BaseModel):
    """ 
    Define como informar nova média e quantidade de avaliações. 
    Fluxo: da API para outra API!!!! Vamos chamar a API que faz a gestão de canoas.

    Método PATCH
    """
    id_canoa: int
    qtde_avaliacoes: int
    media_avaliacoes: float


class SchemaVisualizacaoPostagem(BaseModel):
    """ 
    Define como uma nova postagem recém criada ou excluída deve ser representada. 
    Fluxo: da API para o usuário.
    """
    id_avaliacao: int = 1
    id_canoa: int
    id_usuario: int
    nota: float
    comentario: str = "Totalmente Excelente!"
    


class SchemaVisualizacaoCanoa(BaseModel):
    """ 
    Define como uma nova canoa recém criada ou uma canoa recém excluída deve ser representada. 
    Fluxo: da API para o usuário.
    """
    id_canoa: int = 1
    nome: str = "E Ala E"
    tipo: str = "OC2"
    dono: str = "Fabio"
    qtde_avaliacoes: int
    media_avaliacoes: float
    estado: Optional[str] = "RJ" 
    municipio: Optional[str] = "Rio de Janeiro"
    bairro: Optional[str] = "Glória"
    referencia: Optional[str] = "Aterro do Flamengo"
    latitude: Optional[float] = -22.922477
    longitude: Optional[float] = -43.385915







def comunica_avaliacao_parcial(avaliacao):

    
    """Retorna uma representação da avaliação."""
    return {
        "id_canoa": avaliacao.id_canoa,
        "id_usuario": avaliacao.id_usuario,
        "nota": avaliacao.nota,
        "comentário": avaliacao.comentario,
    }


def comunica_avaliacao_completa(avaliacao, nova_quantidade, nova_media):

    
    """Retorna uma representação da avaliação."""
    return {
        "id_canoa": avaliacao.id_canoa,
        "id_usuario": avaliacao.id_usuario,
        "nota": avaliacao.nota,
        "comentário": avaliacao.comentario,
        "nova media de avaliações": nova_media,
        "nova quantidade de avaliações": nova_quantidade,
    }

def comunica_avaliacao_excluida_completa(postagem, nova_quantidade, nova_media):

    
    """Retorna uma representação da avaliação."""
    return {
        "id_canoa": postagem.id_canoa,
        "id_usuario": postagem.id_usuario,
        "nota": postagem.nota,
        "comentário": postagem.comentario,
        "nova media de avaliações": nova_media,
        "nova quantidade de avaliações": nova_quantidade,
    }