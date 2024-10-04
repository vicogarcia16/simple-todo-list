import flet as ft
from actions.task_actions import add_clicked, delete_checked_tasks

def create_control_panel(page, task_column):
    # Campo de texto para nueva tarea
    new_task = ft.TextField(
        hint_text="What needs to be done?", 
        width=225,
        on_submit=lambda e: add_clicked(e, page, task_column, new_task)  # Añadir tarea cuando se presione Enter
    )

    # Botón para agregar nueva tarea
    add_button = ft.IconButton(
        ft.icons.ADD_CIRCLE_OUTLINED,
        on_click=lambda e: add_clicked(e, page, task_column, new_task),
        icon_size=35,
        icon_color=ft.colors.BLUE
    )

    # Botón para eliminar tareas completadas
    delete_button = ft.IconButton(
        ft.icons.DELETE_ROUNDED,
        on_click=lambda e: delete_checked_tasks(e, page, task_column),
        icon_size=35,
        icon_color=ft.colors.GREEN
    )

    # Contenedor que organiza los controles de la interfaz
    return ft.Container(
        content=ft.Row(
            controls=[new_task, add_button, delete_button],
            alignment="start"
        ),
        margin=ft.Margin(left=25, top=40, right=0, bottom=0)
    )

def create_close_button(page):
    # Mostrar siempre el botón en Android
    visible = page.platform != "android"  # El botón solo será visible por hover en escritorio

    close_button = ft.IconButton(
        ft.icons.CLOSE_OUTLINED,
        on_click=lambda e: e.page.window.close(),
        icon_size=35,
        icon_color=ft.colors.RED,
        visible=visible  # Mostrar o no basado en la plataforma
    )

    # Lógica de hover solo para plataformas no móviles
    def handle_hover(e):
        if page.platform != "android":
            close_button.visible = e.data == "true"
            page.update()

    return ft.Container(
        content=close_button,
        alignment=ft.alignment.center,
        padding=5,
        on_hover=handle_hover if page.platform != "android" else None,  # Deshabilitar hover en Android
        margin=ft.Margin(left=0, top=10, right=0, bottom=0)
    )

