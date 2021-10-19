from sqlalchemy import Column, Integer, String, Float
from database import Base


class Prod(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String)
    valor = Column(Float)
    qtde = Column(String)
