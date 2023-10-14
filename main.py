from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel)


app = QApplication([])
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.show()


app.exec()
