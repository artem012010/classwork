from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QTextEdit,QLineEdit,QListWidget,
    QVBoxLayout,QHBoxLayout)

'''ИНТЕРФЕЙС'''
app = QApplication([])
window = QWidget()
window.setWindowTitle('Умные заметки')
window.resize(900,600)
text_field = QTextEdit()
'''РАЗМЕЩЕНИЕ'''
main_layout = QHBoxLayout()
main_layout.addWidget(text_field)

window.setLayout(main_layout)
window.show()
app.exec()
