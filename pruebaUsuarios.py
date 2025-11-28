# Importamos la clase FastAPI desde el paquete fastapi
from fastapi import FastAPI

#importamos el HTTPException
from fastapi import HTTPException
# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

#Este servicio debe proporcionar dos endpoints GET:

#1º
#"/usuarios/": permite obtener todos los usuarios y devuelve el diccionario db entero.

#2º
#"/usuarios/{usuario_id}": permite obtener información de un usuario específico.
#Si ese usuario no se encuentra en db, debe devolver un mensaje de error.
#(Puedes comprobar si un id no se encuentra en un diccionario con if usuario_id not in db).

#DICCIONARIO QUE ACTUA COMO BD
db = {
    1: {"nombre": "Alice", "edad": 20},
    2: {"nombre": "Bob", "edad": 25},
    3: {"nombre": "Carla", "edad": 30},
}

#1º #"/usuarios/": permite obtener todos los usuarios y devuelve el diccionario db entero.
@app.get("/usuarios/")
def getUsuarios():
    return db
#FatsApi si recibe un diccionario (1: {"nombre": "Alice", "edad": 20},)lo convierte automaticamente en JSON usando librerías internas por eso no es necesario recorrerlo con for 
        

#2º Si ese usuario no se encuentra en db, debe devolver un mensaje de error.
#(Puedes comprobar si un id no se encuentra en un diccionario con if usuario_id not in db).

@app.get("/usuarios/{usuario_id}")
def getUsuarioID(usuario_id: int):
    if usuario_id not in db:
       
            raise HTTPException(status_code=404,detail="Usuario no encontrado")
    else:
        return
            db[usuario_id]
