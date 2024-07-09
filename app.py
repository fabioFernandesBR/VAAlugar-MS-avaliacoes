from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy import func
from flask_graphql import GraphQLView

from models import Session
from models.avaliacao import Avaliacao

from schemas.mensagem_erro import *
from schemas.postagem import *
from schema_graphQL import schema
from logger import logger


from flask_cors import CORS

info = Info(title="VAAlugar-MS-avaliacoes", version="0.1.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# definindo tags
postagem_avaliacao_tag = Tag(name="Postagem de Avaliação", description="Postagem de Avaliação")
exclusao_postagem_tag = Tag(name="Exclusão de Postagem", description="Exclusão de Postagem")
consulta_avaliacao_canoa_tag = Tag(name="Consulta de Avaliações de Canoa", description="Consulta de Avaliações de Canoa")
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")



@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect('/openapi')



@app.post('/criar', tags=[postagem_avaliacao_tag],
          responses={"200": SchemaVisualizacaoPostagem, "409": SchemaMensagemErro, "400": SchemaMensagemErro})
def posta_avaliacao(form: SchemaPostagemAvaliacao):
    """
    Posta uma avaliação

    Retorna uma representação da canoa criada. 
    """
    logger.debug(f"Recebidos dados para postagem de avaliação: {form}")
    print(f"Recebidos dados para postagem de avaliação: {form}")
    avaliacao = Avaliacao(
        id_reserva = form.id_reserva,
        id_canoa = form.id_canoa,
        id_usuario = form.id_usuario,
        nota = form.nota,
        comentario = form.comentario
    )
    print(avaliacao.id_canoa)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando reserva
        session.add(avaliacao)
        # efetivando o comando postagem da avaliação na tabela
        session.commit()
        
        ### Calcula novas estatísticas a respeito da canoa após a inclusão da nota.
        quantidade_avaliacoes = session.query(func.count(Avaliacao.id_avaliacao)).filter_by(id_canoa = avaliacao.id_canoa).scalar()
        media_avaliacoes = session.query(func.avg(Avaliacao.nota)).filter_by(id_canoa = avaliacao.id_canoa).scalar()
        print(f"Quantidade de avaliações para a canoa {avaliacao.id_canoa}: {quantidade_avaliacoes}")
        print(f"Média de avaliações para a canoa {avaliacao.id_canoa}: {media_avaliacoes}")
                    
        return comunica_avaliacao_completa(avaliacao, nova_quantidade = quantidade_avaliacoes, nova_media = media_avaliacoes)
    
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível registrar avaliação : {e}"
        logger.warning(f"Erro ao registrar avaliação, {error_msg}")
        return {"message": error_msg}, 400



@app.delete('/excluir', tags=[exclusao_postagem_tag],
            responses={"200": SchemaVisualizacaoPostagem, "404": SchemaMensagemErro, "400": SchemaMensagemErro})
def exclui_postagem(form: SchemaExclusaoAvaliacao):
    """Exclui uma postagem.

    Retorna uma representação da postagem excluída. 
    """
    logger.debug(f"Recebido dados para exclusão de postagem: {form}")
    try:
        # criando conexão com a base
        session = Session()
        # buscando a postagem a ser excluída
        postagem = session.query(Avaliacao).filter_by(id_avaliacao=form.id_avaliacao).first()
        if postagem is None:
            error_msg = "Postagem não encontrada"
            logger.warning(f"Erro ao excluir post, {error_msg}")
            return {"message": error_msg}, 404

        logger.debug(f"Postagem encontrada: {postagem}")

        # excluindo o post
        session.delete(postagem)
        # efetivando a exclusão no banco de dados
        session.commit()
        logger.debug(f"Postagem excluída do banco de dados: {postagem}")
        
        ### Calcula novas estatísticas a respeito da canoa após a exclusão da nota.
        quantidade_avaliacoes = session.query(func.count(Avaliacao.id_avaliacao)).filter_by(id_canoa = postagem.id_canoa).scalar()
        media_avaliacoes = session.query(func.avg(Avaliacao.nota)).filter_by(id_canoa = postagem.id_canoa).scalar()
        print(f"Quantidade de avaliações para a canoa {postagem.id_canoa}: {quantidade_avaliacoes}")
        print(f"Média de avaliações para a canoa {postagem.id_canoa}: {media_avaliacoes}")
                    
        return comunica_avaliacao_completa(postagem, nova_quantidade = quantidade_avaliacoes, nova_media = media_avaliacoes)

    
    except Exception as e:
        # caso um erro fora do previsto
        session.rollback()  # reverte quaisquer mudanças no banco de dados
        error_msg = f"Não foi possível excluir a canoa: {e}"
        logger.warning(f"Erro ao excluir canoa, {error_msg}")
        return {"message": error_msg}, 400
    finally:
        session.close()


# Configuração do endpoint GraphQL
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Habilita a interface GraphiQL para testar queries
    )
)


if __name__ == '__main__':
    app.run(debug=True)