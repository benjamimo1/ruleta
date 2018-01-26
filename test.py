import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from random import random, randint
from math import sqrt
from PyQt5.QtMultimedia import QSound
from PyQt5.QtTest import QTest

 
class App(QWidget):
 
	def __init__(self):
		super().__init__()
		self.title = 'Ruleta!'
		self.orientacion = 0
		self.girando = False
		self.contador = 0
		self.canciones = [
		QSound("/Users/benjamimo1/Desktop/Ruleta/audio2.wav", self),
		QSound("/Users/benjamimo1/Desktop/Ruleta/audio3.wav", self) ]
		self.initUI()

	def girar(self):

		#Aca especifico pesos del random

		self.orientacion+= 10
		transform = (QTransform().rotate(self.orientacion))
		aux = self.pixmap.copy().transformed(transform)
		self.label.setPixmap(aux)

		

	def initUI(self):
		self.setWindowTitle(self.title)

		# Create widget
		self.label = QLabel(self)
		self.pixmap = QPixmap('/Users/benjamimo1/Desktop/Ruleta/wheel.png')
		diag = (self.pixmap.width()**2 + self.pixmap.height()**2)**0.5
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setPixmap(self.pixmap)
		self.label.setMinimumSize(diag, diag)

		self.label.setMinimumSize(self.label.pixmap().height()*sqrt(2), self.label.pixmap().height()*sqrt(2))

		self.boton = QPushButton("Boton", self)
		self.boton.move(600, 600)
		self.boton.clicked.connect(self.girar)

		self.fondo = QLabel(self)
		self.fondo.setPixmap(QPixmap("/Users/benjamimo1/Desktop/Ruleta/table.jpg"))
		#self.fondo.setGeometry(0, 0, 400, 400)
		self.fondo.lower()

		self.layout = QGridLayout()
		self.layout.addWidget(self.fondo, 0,0)
		self.layout.addWidget(self.label, 0, 0)
		self.layout.addWidget(self.boton, 1,0 )
		

		self.setLayout(self.layout)
		self.show()
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	try:
		sys.exit(app.exec_())
	except Exception as err:
		print(str(err))

#pyinstaller.exe --onefile --windowed app.py