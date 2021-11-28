from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///CorumbaCharadas.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Pontos(Base):
    __tablename__ = 'pontos'
    codigo_ponto = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
        return '<Ponto {}, {}>'.format(self.latitude, self.longitude)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Charadas(Base):
    __tablename__ = 'chadadas'
    id_charada = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(200))
    id_ponto = Column(Integer, ForeignKey('pontos.codigo_ponto'))
    ponto = relationship('Pontos')
    pass


def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()