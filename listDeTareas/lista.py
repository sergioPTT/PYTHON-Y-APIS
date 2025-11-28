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
# @app.post("/tasks/{description}")
# def create_task(description: str):
# #creamos el diccionario:
# nuevaTarea={"id": 3, "description": {description}, "completed": False}
# tasks.append(nuevaTarea)
# return tasks
    

# # Endpoint para marcar una tarea como completada
# @app.put("/tasks/{task_id}")
# def update_task(task_id: int, completed: bool):
#     // ...

# # Endpoint para eliminar una tarea
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     // ...