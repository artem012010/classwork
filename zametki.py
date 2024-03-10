from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QListWidget,QTextEdit,QLineEdit

app = QApplication([]) # Создаем приложение
'''СОЗДАНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА'''
window = QWidget() # Создаем окошко
window.setWindowTitle('Умные заметки') # Добовляем название окна
text_field = QTextEdit() # Поле с текстом
'''РАСПОЛОЖЕНИЕ ВИДЖЕТОВ'''
main_layout = QVBoxLayout() # Создаем вертикальный макет
main_layout.addWidget(text_field) # Добовляем в него виджет с текстом


window.setLayout(main_layout) # Устанавливаем главную линию к окну
window.show() # Показать окно
app.exec() # Не закрывать до нажатия крестика
