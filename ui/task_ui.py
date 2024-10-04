import flet as ft
from db.db_task import save_all_tasks, load_tasks

def add_task_to_column(page, task_column, task):
    checkbox = ft.Checkbox(label=task["label"], value=task["completed"])

    def checkbox_changed(e):
        # Actualizar el estado de la tarea
        task["completed"] = checkbox.value
        # Cargar todas las tareas del archivo JSON
        tasks = load_tasks(page)
        # Buscar la tarea en la lista y actualizar su estado
        for t in tasks:
            if t["id"] == task["id"]:
                t["completed"] = task["completed"]
        # Guardar todas las tareas con el estado actualizado
        save_all_tasks(page, tasks)

    checkbox.on_change = checkbox_changed

    task_panel = ft.Card(
        content=ft.Container(
            content=ft.Row(controls=[checkbox], alignment="start"),
            padding=10
        ),
        margin=ft.Margin(left=25, top=10, right=30, bottom=-10)
    )

    task_panel.task_id = task["id"]
    task_panel.checkbox = checkbox
    task_column.controls.append(task_panel)
    page.update()
