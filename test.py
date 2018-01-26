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
		self.premios = ["Llavero tipo Casco","Bolsa ecológica","Reposa cabeza"]
		self.canciones = [
		QSound("/Users/benjamimo1/Desktop/Ruleta/audio4.wav", self),
		QSound("/Users/benjamimo1/Desktop/Ruleta/audio3.wav", self) ]
		self.initUI()

	def girar(self):
		
		#resultados simulacion {'llavero': 301, 'bolsa': 98, 'reposa': 101}
		self.orientacion = 5
		self.contador = randint(60,100)
		self.canciones[0].play()

		while self.contador>0:
			print(self.orientacion)
			self.orientacion+= 9
			transform = (QTransform().rotate(self.orientacion))
			aux = self.pixmap.copy().transformed(transform)
			self.label.setPixmap(aux)

			if self.contador>20:  #Desaceleracion
				QTest.qWait(45)

			elif self.contador>10:
				QTest.qWait(65)

			else:
				QTest.qWait(90)

			self.contador-=1

		self.canciones[0].stop()
		self.canciones[1].play()

		valor_final = (self.orientacion%360)//36+1

		if valor_final <=6:
			premio = self.premios[0]
		elif valor_final <=8:
			premio = self.premios[1]
		elif valor_final <=10:
			premio = self.premios[2]

		print("Ha salido {}".format(premio))



	def initUI(self):
		self.setWindowTitle(self.title)

		# Create widget
		self.label = QLabel(self)
		self.pixmap = QPixmap('/Users/benjamimo1/Desktop/Ruleta/ruletaColornumero.png')
		diag = (self.pixmap.width()**2 + self.pixmap.height()**2)**0.5
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setPixmap(self.pixmap)
		self.label.setMinimumSize(diag, diag)
		self.label.lower()

		self.label.setMinimumSize(self.label.pixmap().height()*sqrt(2), self.label.pixmap().height()*sqrt(2))

		self.boton = QPushButton("A Jugar!", self)
		self.boton.move(600, 600)
		self.boton.clicked.connect(self.girar)

		self.logo = QLabel(self)
		self.logoPixmap = QPixmap('/Users/benjamimo1/Desktop/Ruleta/logo.JPG')
		self.logo.setPixmap(self.logoPixmap.scaledToHeight(100))

		self.triangulo = QLabel(self)
		self.triangulo.setPixmap(QPixmap("/Users/benjamimo1/Desktop/Ruleta/triangulo.png").scaledToHeight(50))
		self.triangulo.move(440, 130)
		self.triangulo.raise_()

		self.layout = QGridLayout()
		#self.layout.addWidget(self.fondo, 0,0)
		self.layout.addWidget(self.label, 0, 0)
		self.layout.addWidget(self.logo, 1, 0)
		self.layout.addWidget(self.boton, 2,0 )
		self.layout.setSpacing (5)
		self.layout.setSizeConstraint(QLayout.SetFixedSize)
		self.setLayout(self.layout)
		#self.setFixedSize(,)
		self.show()

		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	try:
		sys.exit(app.exec_())
	except Exception as err:
		print(str(err))

#pyinstaller.exe --onefile --windowed app.py