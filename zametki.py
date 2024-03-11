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

notes_list = QListWidget()
create_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить заметку')
save_note = QPushButton('Сохранить заметку')
'''РАЗМЕЩЕНИЕ'''
main_layout = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
v1.addWidget(text_field)
v2.addWidget(notes_list)
v2.addWidget(create_note)
v2.addWidget(delete_note)
v2.addWidget(save_note)
main_layout.addLayout(v1)
main_layout.addLayout(v2)

window.setLayout(main_layout)
window.show()
app.exec()
