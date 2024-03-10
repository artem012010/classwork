from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QListWidget,QTextEdit,QLineEdit

app = QApplication([]) # Создаем приложение
'''СОЗДАНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА'''
window = QWidget() # Создаем окошко
window.setWindowTitle('Умные заметки') # Добовляем название окна
text_field = QTextEdit() # Поле с текстом
notes_list = QListWidget() # Список с заметками
tag_list = QListWidget() # Список с тегами
'''РАСПОЛОЖЕНИЕ ВИДЖЕТОВ'''
main_layout = QVBoxLayout() # Создаем вертикальный макет
main_layout.addWidget(text_field) # Добавляем  виджет с текстом
main_layout.addWidget(notes_list) # Добавляем виджет cписка заметок
main_layout.addWidget(tag_list) # Добавляем виджет cписка тегов
'''ЗАПУСК'''
window.setLayout(main_layout) # Устанавливаем главную линию к окну
window.show() # Показать окно
app.exec() # Не закрывать до нажатия крестика
