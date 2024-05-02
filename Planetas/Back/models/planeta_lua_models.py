from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.configs import settings

class LuaModel(settings.DBBaseModel):
    __tablename__ = 'lua'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    planeta_id: int = Column(Integer, ForeignKey('planeta.id'))

    # Define o relacionamento com PlanetaModel
    planeta = relationship("PlanetaModel", back_populates="luas")

class PlanetaModel(settings.DBBaseModel):
    __tablename__ = 'planeta'

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    temperatura_media: int = Column(Integer())
    ano : str = Column(String(50))
    rotacao: str = Column(String(50))
    translacao: str = Column(String(50))

    # Defina o relacionamento com LuaModel
    luas = relationship("LuaModel", back_populates='planeta', lazy='joined')
