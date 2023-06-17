from database import Base, engine

# generando las tablas en la base de datos utilizando el modelo definido en Base y engine.
Base.metadata.create_all(engine)