from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint
 
app = QApplication([])
 
# главное окно:
my_win = QWidget()


my_win.show()
app.exec_()
