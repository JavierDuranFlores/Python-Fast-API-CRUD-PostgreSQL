from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# configuración básica para la conexión a la base de datos

engine = create_engine("postgresql://postgres:Duran2001@localhost:5432/fast_api_rest",
    echo=True
)

Base = declarative_base()

SessionLocal=sessionmaker(bind=engine)