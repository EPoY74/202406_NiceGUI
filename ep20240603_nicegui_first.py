'''
Тыкаю палкой
'''

from nicegui import ui

# Создаем простое приложение с кнопкой и элементами ввода

with ui.row():
    ui.button('Нажми меня', on_click=lambda: ui.notify('Клик!'))
    ui.input('Текстовое поле', on_change=lambda event: ui.notify(f'Изменено: {event.value}'))


ui.run()