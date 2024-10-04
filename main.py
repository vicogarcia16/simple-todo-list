import flet as ft
from db.db_task import load_tasks
from config.config_page import config_page_sf
from ui.task_ui import add_task_to_column
from ui.buttons_ui import create_control_panel, create_close_button

def main(page: ft.Page):
    page.title = "TODO List"
    config_page_sf(page)

    # Cargar las tareas desde el archivo JSON
    tasks = load_tasks(page)  # Pasar la instancia de la página para manejar rutas en Android
    
    # Crear la columna para las tareas
    task_column = ft.Column()

    # Crear los botones
    control_panel = create_control_panel(page, task_column)
    close_button = create_close_button(page)

    # Cargar tareas previamente guardadas y agregarlas a la columna de tareas
    for task in tasks:
        add_task_to_column(page, task_column, task)

    # Organizar la interfaz y agregarla a la página
    page.add(
        ft.Column(
            controls=[
                control_panel,  # Controles para añadir y eliminar tareas
                task_column,    # Columna donde se muestran las tareas
                close_button    # Botón para cerrar la ventana
            ],
            expand=True,
        )
    )

# Ejecutar la aplicación Flet
ft.app(target=main)
