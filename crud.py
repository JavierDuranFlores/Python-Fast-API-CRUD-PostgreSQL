
from database import SessionLocal
from models import Usuario
from sqlalchemy import text

def create(db: SessionLocal, usuario: Usuario):
    nuevo_usuario = Usuario(
        usuario_id=usuario.usuario_id,
        nombre=usuario.nombre,
        usuario=usuario.usuario,
        password=usuario.password,
        telefono=usuario.telefono
    )
    
    query = text(f"SELECT usuarios({nuevo_usuario.usuario_id}, '{nuevo_usuario.nombre}', '{nuevo_usuario.usuario}', '{nuevo_usuario.password}', '{nuevo_usuario.telefono}');")
    db.execute(query)
    db.commit()
    db.close()
    
    return nuevo_usuario

def read(db: SessionLocal):
    query = text("SELECT * FROM vista_usuarios;")
    result=db.execute(query)
    usuarios=result.fetchall()
    db.close()
    
    return usuarios;

def update(db: SessionLocal, usuario_id: int, usuario: Usuario):
    
    usuario_actualizar=db.query(Usuario).filter(Usuario.usuario_id==usuario_id).first()
    usuario_actualizar.nombre=usuario.nombre
    usuario_actualizar.usuario=usuario.usuario
    usuario_actualizar.password=usuario.password
    usuario_actualizar.telefono=usuario.telefono
    
    db.commit()
    
    return usuario_actualizar

def delete(db: SessionLocal, usuario_id: int):
    
    query = text(f"SELECT eliminar_usuario({usuario_id});")
    db.execute(query)    
    db.commit()
    db.close()

def exists_user(db: SessionLocal, usuario_id: int):
    query = text(f"SELECT * FROM obtener_usuario({usuario_id});")
    print(query)
    result=db.execute(query)
    usuario=result.fetchone()
    db.close()
    
    return usuario
    