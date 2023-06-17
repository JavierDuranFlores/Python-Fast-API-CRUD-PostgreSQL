from sqlalchemy import text
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from werkzeug.security import generate_password_hash
import crud

app = FastAPI()

class Usuario(BaseModel):
    usuario_id: int
    nombre: str
    usuario: str
    password: str
    telefono: str
    
    class Config:
        orm_mode=True
        
db = SessionLocal()

@app.get("/usuarios", response_model=List[Usuario], status_code=200)
async def obtener_usuarios():
    
    usuarios = crud.read(db)
    
    if len(usuarios) == 0:
        raise HTTPException(status_code=400, detail="No hay usuarios")
    
    return usuarios

@app.get("/usuarios/{usuario_id}", response_model=Usuario, status_code=status.HTTP_200_OK)
async def obtener_usuario(usuario_id: int):
    usuario = crud.exists_user(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=400, detail="Usuario no existe")
    
    return usuario

@app.post("/usuarios", response_model=Usuario, 
          status_code=status.HTTP_201_CREATED)
async def crear_usuario(usuario: Usuario):
    new_user = Usuario(
        usuario_id=usuario.usuario_id,
        nombre=usuario.nombre,
        usuario=usuario.usuario,
        password=generate_password_hash(usuario.password, "pbkdf2:sha256:30", 30),
        telefono=usuario.telefono
    )
    return crud.create(db, new_user)

@app.put("/usuario/{usuario_id}", response_model=Usuario, status_code=status.HTTP_200_OK)
async def actualizar_usuario(usuario_id: int, usuario: Usuario):
    if crud.exists_user(db, usuario_id) is None:
        raise HTTPException(status_code=400, detail="Usuario no existe")
    
    new_user = Usuario(
        usuario_id=usuario.usuario_id,
        nombre=usuario.nombre,
        usuario=usuario.usuario,
        password=generate_password_hash(usuario.password, "pbkdf2:sha256:30", 30),
        telefono=usuario.telefono
    )
    
    return crud.update(db, usuario_id, new_user)
    

@app.delete("/usuario/{usuario_id}")
async def eliminar_usuario(usuario_id: int):
    if crud.exists_user(db, usuario_id) is None:
        raise HTTPException(status_code=400, detail="Usuario no existe")
    
    crud.delete(db, usuario_id)
    return HTTPException(status_code=200, detail="Usuario eliminado con exito")