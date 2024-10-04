import uuid
from ui.task_ui import add_task_to_column
from db.db_task import load_tasks, save_task, delete_task

def add_clicked(e, page, task_column, new_task):
    label = new_task.value.strip()
    if label:
        task = {
            "id": str(uuid.uuid4()),
            "label": label,
            "completed": False
        }
        save_task(task)  # Guardar la nueva tarea en el archivo JSON
        add_task_to_column(page, task_column, task)
        new_task.value = ""
        page.update()

def delete_checked_tasks(e, page, task_column):
    checked_ids = []
    for task_panel in task_column.controls:
        checkbox = task_panel.checkbox
        if checkbox.value:
            task_id = task_panel.task_id
            checked_ids.append(task_id)

    delete_task(checked_ids)  # Eliminar las tareas marcadas en el archivo JSON
    task_column.controls.clear()

    tasks = load_tasks()  # Volver a cargar las tareas
    for task in tasks:
        if not task["completed"]:
            add_task_to_column(page, task_column, task)

    page.update()
