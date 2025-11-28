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
    return {"message": "Esto es una API CALCULADORA",
            "result": "pon: /operacion/numero1/numero2 en la URL"
    
    }

#suma
@app.get("/suma/{num1}/{num2}")
def sumaValores(num1: int, num2: int):
    return {
       "message": f"vamos a sumar los valores {num1} y {num2}",
        "resultado": f"el resultado es: {sum([num1, num2])}"
    }

#resta
@app.get("/resta/{num1}/{num2}")
def restaValores(num1: int, num2: int):
    result = num1 - num2;
    return{
        "message": f"los valores que vamos a restas son {num1} y {num2}",
        "resultado": f"el resultado es: {result}"
    }
#multiplicacion
@app.get("/multiplicacion/{num1}/{num2}")
def multiValores(num1: int, num2: int):
    result= num1 * num2;
    return{
        "message": f"Los valores que queremos multiplicar son {num1} y {num2}",
        "result": f"el resultado de la operacion es: {result}"
    }

#division
@app.get("/division/{num1}/{num2}")
def divisionValores(num1: int , num2: int):
    result= num1/num2;
    return{
        "message": f"los valores que vas a dividir son {num1} y {num2}",
        "resultado": f"el resultado es: {result}"
    }
