import os
import json
import flet as ft

# Archivo de tareas
TASKS_FILE = "tasks.json"

# Obtener la ruta de almacenamiento privado en Android
def get_tasks_file_path(page: ft.Page):
    if page.platform == "android":
        # Obtener el directorio de almacenamiento interno privado de la aplicación
        app_data_dir = page.get_application_directory()
        tasks_file_path = os.path.join(app_data_dir, TASKS_FILE)
        
        # Si el archivo no existe en el almacenamiento interno, copiar desde assets
        if not os.path.exists(tasks_file_path):
            asset_file = page.get_asset(TASKS_FILE)
            with open(tasks_file_path, "wb") as f_out:
                f_out.write(asset_file.read())
        return tasks_file_path
    else:
        return TASKS_FILE  # Para entornos locales o escritorio

# Cargar las tareas del archivo JSON
def load_tasks(page: ft.Page):
    tasks_file_path = get_tasks_file_path(page)
    if os.path.exists(tasks_file_path):
        with open(tasks_file_path, "r") as f:
            return json.load(f)
    return []

# Guardar una nueva tarea en el archivo JSON
def save_task(page: ft.Page, task):
    tasks = load_tasks(page)
    tasks.append(task)
    tasks_file_path = get_tasks_file_path(page)
    with open(tasks_file_path, "w") as f:
        json.dump(tasks, f)

# Guardar todas las tareas en el archivo JSON (sobrescribir todo)
def save_all_tasks(page: ft.Page, tasks):
    tasks_file_path = get_tasks_file_path(page)
    with open(tasks_file_path, "w") as f:
        json.dump(tasks, f)

# Eliminar tareas marcadas y actualizar el archivo JSON
def delete_task(page: ft.Page, checked_ids):
    tasks = load_tasks(page)
    tasks = [task for task in tasks if task["id"] not in checked_ids]
    tasks_file_path = get_tasks_file_path(page)
    with open(tasks_file_path, "w") as f:
        json.dump(tasks, f)
