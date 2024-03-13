from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                     QLabel, QPushButton, QVBoxLayout)
'''ИНТЕРФЕЙС'''
app = QApplication([])
window = QWidget()
window.setWindowTitle('Определить победителя')
window.resize(400,200)

text = QLabel('Кто красавчик?')
winner = QLabel('?')
button = QPushButton('Сгенерировать')

layout = QVBoxLayout()
'''РАЗМЕЩЕНИЕ'''

layout.addWidget(text, alignment=Qt.AlignCenter)
layout.addWidget(winner, alignment=Qt.AlignCenter)
layout.addWidget(button)

window.setLayout(layout)

def show_winner():
    winner.setText(['Кутман','Роман','Арсений','Артем'][randint(0,3)])

button.clicked.connect(show_winner)

window.show()
app.exec()
