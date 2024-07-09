from graphene import Int, List, ObjectType, Schema, String
from graphene_sqlalchemy import SQLAlchemyObjectType
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from models.avaliacao import Avaliacao as AvaliacaoDBmodel


# Definição de tipos GraphQL usando SQLAlchemyObjectType
class AvaliacaoSchemaGraphQL(SQLAlchemyObjectType):
    class Meta:
        model = AvaliacaoDBmodel
        

    # Mapeamento de campos
    idPost = Int(source='id_avaliacao')  # Mapeando idPost para id_avaliacao no modelo SQLAlchemy
    idReserva = Int(source ='id_reserva')
    idCanoa = Int(source='id_canoa')
    idUsuario = String(source='id_usuario')




# Definição de consultas GraphQL

class Query(ObjectType):
    posts = List(AvaliacaoSchemaGraphQL, idCanoa = Int(), idUsuario = Int(), idReserva = Int())

    def resolve_posts(self, info, idCanoa=None, idUsuario=None, idReserva = None):
        query = AvaliacaoSchemaGraphQL.get_query(info)  # SQLAlchemy query

        if idCanoa:
            query = query.filter(AvaliacaoDBmodel.id_canoa == idCanoa)    

        if idUsuario:
            query = query.filter(AvaliacaoDBmodel.id_usuario == idUsuario)

        if idReserva:
            query = query.filter(AvaliacaoDBmodel.id_reserva == idReserva)

        return query.all()



schema = Schema(query=Query)