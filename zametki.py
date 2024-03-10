from PyQt5.QtWidgets import (
    QApplication,QWidget,QPushButton,QTextEdit,
    QLineEdit,QListWidget,QVBoxLayout,QHBoxLayout
)
# НАСТРОЙКА ОКНА
app = QApplication([]) # создаем приложение
window = QWidget() # создаем окно
window.setWindowTitle('Умные заметки') # Меняем название окна
window.resize(900,600) # Меняем размер окна
# СОЗДАНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА
text_field = QTextEdit() # Текстовое поле
notes_list = QListWidget() # Создаем список с заметками
create_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить заметку')
save_note = QPushButton('Сохранть заметку')

tags_list = QListWidget() # Создаем список с заметками
add_tag = QPushButton('Добавить тег')
delete_tag = QPushButton('Открепить тег')
search = QPushButton('Поиск')
tag_field = QLineEdit()
#РАЗМЕЩЕНИЕ ВИДЖЕТОВ
main_layout = QHBoxLayout() # Создаем главную горизонтальную линию
v1 = QVBoxLayout() # Вертикальная линия для поля с текстом
v2 = QVBoxLayout() # Вертикальная линия для списков
h1 = QHBoxLayout() # Горизонтальная линия для кнопок сохранить и удалить
h2 = QHBoxLayout()
h3 = QHBoxLayout() # Горизонтальная линия для кнопок добавить и открепить
v1.addWidget(text_field) 
v2.addWidget(notes_list)
h1.addWidget(create_note)
h1.addWidget(delete_note)
v2.addLayout(h1)
v2.addWidget(save_note)
v2.addWidget(tags_list)
h2.addWidget(add_tag)
h2.addWidget(delete_tag)
v2.addLayout(h2)
h3.addWidget(search)
h3.addWidget(tag_field)
v2.addLayout(h3)
main_layout.addLayout(v1) # Добавляем линию с полем ввода текста на главную линию
main_layout.addLayout(v2) # Добавляем линию со списками на главную линию
window.setLayout(main_layout) # Добавляем главную линию к окну

window.show() # показываем окно
app.exec() # просим приложение не закрываться до нажатия на крестик
