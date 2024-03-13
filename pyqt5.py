from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                     QLabel, QPushButton, QVBoxLayout)
'''ИНТЕРФЕЙС'''
app = QApplication([])
window = QWidget()
text = QLabel('Нажми чтобы узнать победителя!')
winner = QLabel('?')
button = QPushButton('Сгенерировать')
layout = QVBoxLayout()
'''РАЗМЕЩЕНИЕ'''
layout.addWidget(text, alignment=Qt.AlignCenter)
layout.addWidget(winner, alignment=Qt.AlignCenter)
layout.addWidget(button)

window.setLayout(layout)

window.show()
app.exec()
