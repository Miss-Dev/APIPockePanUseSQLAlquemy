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
    __tablename__ = 'charadas'
    id_charada = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(200))
    id_ponto = Column(Integer, ForeignKey('pontos.codigo_ponto'))
    ponto = relationship('Pontos')

    def __repr__(self):
        return '<Charada {}>'.format(self.descricao)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Pontuacao(Base):
    __tablename__ = 'pontuacao'
    id_pontuacao = Column(Integer, primary_key=True, autoincrement=True)
    primeiro_vencedor = Column(Integer)
    segundo_vencedor = Column(Integer)
    terceiro_vencedor = Column(Integer)
    id_charada = Column(Integer, ForeignKey('charadas.id_charada'))
    charada = relationship('Charadas')

    def __repr__(self):
        return '<Pontuacao\n primeiro: {}, segundo: {}, terceiro: {}>'.format(self.primeiro_vencedor, self.segundo_vencedor, self.terceiro_vencedor)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))

    def __repr__(self):
        return '<Usuário {}>'.format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
