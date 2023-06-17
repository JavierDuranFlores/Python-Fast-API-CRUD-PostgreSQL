from database import Base
from sqlalchemy import  Column, Integer, String

class Usuario(Base):
    __tablename__ ="usuarios"
    
    usuario_id = Column(Integer, primary_key=True, index=True, unique=True, nullable=True)
    nombre = Column(String(30), nullable=True)
    usuario = Column(String(30), nullable=True)
    password = Column(String(250), nullable=True)
    telefono = Column(String(30), nullable=True)