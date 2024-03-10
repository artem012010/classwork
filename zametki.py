from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QListWidget,QTextEdit,QLineEdit

app = QApplication([]) # Создаем приложение
'''СОЗДАНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА'''
window = QWidget() # Создаем окошко
window.setWindowTitle('Умные заметки') # Добовляем название окна
window.resize(900,600)
text_field = QTextEdit() # Поле с текстом
notes_list = QListWidget() # Список с заметками
create_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить заметку')
save_note = QPushButton('Сохранить заметку')
tag_list = QListWidget() # Список с тегами
add_tag = QPushButton('Добавить тег')
delete_tag = QPushButton('Удалить тег')
search = QPushButton('Поиск')
tag_field = QLineEdit()
tag_field.setPlaceholderText('Введите тег . . .')
'''РАСПОЛОЖЕНИЕ ВИДЖЕТОВ'''
main_layout = QHBoxLayout() # Создаем главную линию
text_layout = QVBoxLayout() # Создаем линию для поля ввода текста
text_layout.addWidget(text_field) # Добавляем виджет
main_layout.addLayout(text_layout) # Закрепляем линию с текстом на главной линии
list_layout = QVBoxLayout() # Создаем линию для списков
list_layout.addWidget(notes_list)

list_buttons_layout = QHBoxLayout()
list_buttons_layout.addWidget(create_note)
list_buttons_layout.addWidget(delete_note)
list_layout.addLayout(list_buttons_layout)

list_layout.addWidget(save_note)

list_layout.addWidget(tag_list)
list_layout.addWidget(add_tag)
list_layout.addWidget(delete_tag)

list_tags_layout = QHBoxLayout()
list_tags_layout.addWidget(add_tag)
list_tags_layout.addWidget(delete_tag)
list_layout.addLayout(list_tags_layout)

list_layout.addWidget(tag_field)
list_layout.addWidget(search)
main_layout.addLayout(list_layout)
'''ЗАПУСК'''
window.setLayout(main_layout) # Устанавливаем главную линию к окну
window.show() # Показать окно
app.exec() # Не закрывать до нажатия крестика
