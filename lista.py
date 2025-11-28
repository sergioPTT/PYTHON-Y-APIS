from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# Lista de tareas simulada
tasks = [
    {"id": 1, "description": "Hacer la compra", "completed": False},
    {"id": 2, "description": "Pagar las facturas", "completed": False},
]

@app.get("/")
def read_tasks():
    return{
        "message": "Esta es la lista de tareas!!"
    }

# Endpoint para obtener todas las tareas
@app.get("/tasks/")
def read_tasks():
    return tasks

# # Endpoint para obtener una tarea por su ID
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
           return task
    raise HTTPException(status_code=404,detail="Tarea no encontrado")
    
 
# # Endpoint para crear una nueva tarea 
@app.post("/tasks/{description}")
def create_task(description: str):
#recorremos la lista de tareas hasta enocntrar el ultimo ID
   idMayor = max(task["id"] for task in tasks)
   idMayor+=1
#creamos el diccionario:
    nuevaTarea={"id": idMayor, "description": {description}, "completed": False}
    tasks.append(nuevaTarea)
    return nuevaTarea
    

# # Endpoint para marcar una tarea como completada
from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [
    {"id": 1, "description": "Hacer la compra", "completed": False},
    {"id": 2, "description": "Pagar las facturas", "completed": False},
]

@app.put("/tasks/{task_id}")
def update_task(task_id: int, completed: bool):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = completed
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# # Endpoint para eliminar una tarea
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     // ...