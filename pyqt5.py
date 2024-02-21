from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton

app = QApplication([]) # создаем приложение
main_win = QWidget() # создаем окно

main_win.show() # Показать окно
app.exec_() # Закрытие по крестику
