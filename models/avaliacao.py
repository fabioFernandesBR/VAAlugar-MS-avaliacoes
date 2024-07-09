from sqlalchemy import Column, String, Integer, Numeric
from models import Base


class Avaliacao(Base):
    __tablename__ = 'avaliacoes'

    id_avaliacao = Column(Integer, primary_key = True)
    id_canoa = Column(Integer)
    id_usuario = Column(String(256))
    nota = Column(Numeric())
    comentario = Column(String(280))
    id_reserva = Column(Integer)

    
    def __init__(self, id_reserva, id_canoa, id_usuario, nota, comentario = None):
        
        # Cria uma Avaliação!

               
        self.id_reserva = id_reserva
        self.id_canoa = id_canoa
        self.id_usuario = id_usuario
        self.nota = nota
        self.comentario = comentario
       

        