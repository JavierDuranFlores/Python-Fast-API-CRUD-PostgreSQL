# __Fast API__

Esta API REST fue desarrollada utilizando FastAPI en Python y se conecta a una base de datos PostgreSQL. Proporciona operaciones CRUD (Crear, Leer, Actualizar y Eliminar) para gestionar usuarios.

## Endpoints de la API

A continuación se muestra un resumen de los endpoints disponibles en la API:


| Endpoint                  | Método | Descripción                                |
|---------------------------|--------|--------------------------------------------|
| `/usuarios`               | GET    | Retorna una lista de usuarios              |
| `/usuarios/{usuario_id}`  | GET    | Retorna un usuario específico por su ID    |
| `/usuarios`               | POST   | Crea un nuevo usuario                      |
| `/usuarios/{usuario_id}`  | PUT    | Actualiza un usuario existente por su ID   |
| `/usuarios/{usuario_id}`  | DELETE | Elimina un usuario existente por su ID     |


## Descripcion de los Endpoints
### Obtener Usuarios
Retorna una lista de usuarios.


* __URL:__ /usuarios
* __Método:__ GET
* __Parámetros de consulta:__ Ninguno
* __Código de respuesta exitosa:__ 200 (OK)
* __Código de respuesta de error:__ 400 (Bad Request)

#### Ejemplo de solicitud

GET /usuarios

#### Ejemplo de respuesta
```json
[
  {
    "usuario_id": 1,
    "nombre": "John Doe",
    "usuario": "johndoe",
    "password": "john123",
    "telefono": "123456789"
  },
  {
    "usuario_id": 2,
    "nombre": "Jane Smith",
    "usuario": "janesmith",
    "password": "jane123",
    "telefono": "987654321"
  }
]
```

### Obtener Usuario por ID
Retorna un usuario específico basado en el ID proporcionado.

* __URL:__ /usuarios/{usuario_id}
* __Método:__ GET
* __Parámetros de consulta:__ usuario_id (entero)
* __Código de respuesta exitosa:__ 200 (OK)
* __Código de respuesta de error:__ 400 (Bad Request), 404 (Not Found)

#### Ejemplo de solicitud
GET /usuarios/1

#### Ejemplo de respuesta
```json
{
  "usuario_id": 1,
  "nombre": "John Doe",
  "usuario": "johndoe",
  "password": "john123",
  "telefono": "123456789"
}
```

### Crear Usuario
Crea un nuevo usuario en la base de datos.

* __URL:__ /usuarios
* __Método:__ POST
* __Parámetros de consulta:__ Ninguno
* __Código de respuesta exitosa:__ 201 (Created)
* __Código de respuesta de error:__ 400 (Bad Request)

#### Ejemplo de solicitud
POST /usuarios
```json
{
  "usuario_id": 3,
  "nombre": "Alice Smith",
  "usuario": "alicesmith",
  "password": "alice123",
  "telefono": "555555555"
}
```
#### Ejemplo de respuesta
```json
{
  "usuario_id": 3,
  "nombre": "Alice Smith",
  "usuario": "alicesmith",
  "password": "alice123",
  "telefono": "555555555"
}
```
### Actualizar Usuario
Actualiza un usuario existente en la base de datos.

* __URL:__ /usuarios/{usuario_id}
* __Método:__ PUT
* __Parámetros de consulta:__ usuario_id (entero)
* __Código de respuesta exitosa:__ 200 (OK)
* __Código de respuesta de error:__ 400 (Bad Request), 404 (Not Found)

#### Ejemplo de solicitud

PUT /usuarios/1
```json
{
  "usuario_id": 1,
  "nombre": "John Doe",
  "usuario": "johndoe1234",
  "password": "123444",
  "telefono": "987654321"
}
```
#### Ejemplo de respuesta
```json
{
  "usuario_id": 1,
  "nombre": "John Doe",
  "usuario": "johndoe",
  "password": "123444"
  "telefono": "987654321"
}
```

### Eliminar Usuario

Elimina un usuario existente de la base de datos.

* __URL:__ /usuarios/{usuario_id}
* __Método:__ DELETE
* __Parámetros de consulta:__ usuario_id (entero)
* __Código de respuesta exitosa:__ 200 (OK)
* __Código de respuesta de error:__ 400 (Bad Request), 404 (Not Found)

#### Ejemplo de solicitud
PUT /usuarios/1


#### Ejemplo de respuesta
```json
{
  "status_code": 200,
  "detail": "Usuario eliminado con exito",
  "headers": null
}
```