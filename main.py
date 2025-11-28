
# Importamos la clase FastAPI desde el paquete fastapi
from fastapi import FastAPI

# Importamos la clase datetime para trabajar con fechas y horas
from datetime import datetime

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Definimos una ruta GET en la raíz "/" de la API
@app.get("/")
def read_root():
    # Retorna un diccionario (que FastAPI convierte en JSON) con un mensaje de bienvenida
    return {"message": "Bienvenido a mi API"}

# Definimos una ruta GET que recibe un parámetro 'nombre' en la URL
@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    # Obtenemos la fecha actual y la formateamos en el formato Año-Mes-Día
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    # Retornamos un mensaje personalizado usando f-string con el nombre y la fecha actual
    return {
        "message": f"Hola {nombre}, hoy es {fecha_actual}"
    }

# Definimos una ruta GET que recibe un texto y devuelve su longitud
@app.get("/lentexto/{texto}")
def len_texto(texto: str):
    # Retornamos el texto original y su longitud calculada con len()
    return {
        "texto": texto,
        "longitud": len(texto)
    }

@app.get("/dungeon/{message}")
def mensaggeOfDungeon(message):
    return{
        "texto": f"cuando juege al ODD sere la: {message}"
    }