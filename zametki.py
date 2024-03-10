from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QListWidget,QTextEdit,QLineEdit

app = QApplication([]) # Создаем приложение
'''СОЗДАНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА'''
window = QWidget() # Создаем окошко
window.setWindowTitle('Умные заметки') # Добовляем название окна
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
main_layout = QVBoxLayout() # Создаем вертикальный макет
main_layout.addWidget(text_field) # Добавляем  виджет с текстом
main_layout.addWidget(notes_list) # Добавляем виджет cписка заметок
main_layout.addWidget(tag_list) # Добавляем виджет cписка тегов
'''ЗАПУСК'''
window.setLayout(main_layout) # Устанавливаем главную линию к окну
window.show() # Показать окно
app.exec() # Не закрывать до нажатия крестика
