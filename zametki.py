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

tags_list = QListWidget()
create_tag = QPushButton('Добавить тег')
delete_tag = QPushButton('Удалить тег')
search = QPushButton('Поиск:')
search_field = QLineEdit()

'''РАЗМЕЩЕНИЕ'''
main_layout = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
v1.addWidget(text_field)
v2.addWidget(notes_list)
h1.addWidget(create_note)
h1.addWidget(delete_note)
v2.addLayout(h1)
v2.addWidget(save_note)
v2.addWidget(tags_list)
h3.addWidget(create_tag)
h3.addWidget(delete_tag)
v2.addLayout(h2)
h2.addWidget(search)
h2.addWidget(search_field)
v2.addLayout(h3)

main_layout.addLayout(v1)
main_layout.addLayout(v2)

window.setLayout(main_layout)
window.show()
app.exec()
