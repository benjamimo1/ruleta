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

		#self.orientacion+= 10
		#transform = (QTransform().rotate(self.orientacion)
		#aux = self.pixmap.copy().transformed(transform)
		#self.label.setPixmap(aux)

		self.contador = randint(35,45)
		self.orientacion = 0
		self.canciones[0].play()

		while self.contador>0:
			if self.orientacion == 19:
				self.orientacion = -1
			self.orientacion+=1
			aux = self.imagenes[self.orientacion]
			self.label.setPixmap(aux.scaledToHeight(400))
			print(self.orientacion)
			if self.contador>10:
				QTest.qWait(75)
			else:
				QTest.qWait(90)
			self.contador-=1
		self.canciones[0].stop()
		self.canciones[1].play()

		

	def initUI(self):
		self.setWindowTitle(self.title)

		# Create widget
		#self.label = QLabel(self)
		#self.pixmap = QPixmap('/Users/benjamimo1/Desktop/Ruleta/wheel.png')
		#self.label.setPixmap(self.pixmap)
		#self.resize(self.pixmap.width(),self.pixmap.height())
		#self.label.setMinimumSize(self.label.pixmap().height()*sqrt(2), self.label.pixmap().height()*sqrt(2))
		
		self.sprite = QPixmap("/Users/benjamimo1/Desktop/Ruleta/pie.gif")
		self.imagenes = []

		for i in range(20):
			rect = QRect(0 + 512 * i, 0, 512, 512)
			circulo = self.sprite.copy(rect)
			imagen = circulo.scaledToHeight(400)
			self.imagenes.append(imagen)


		self.label = QLabel(self)
		self.label.setPixmap(self.imagenes[self.orientacion].scaledToHeight(400))

		self.boton = QPushButton("Boton", self)
		self.boton.move(600, 600)
		self.boton.clicked.connect(self.girar)

		self.fondo = QLabel(self)
		self.fondo.setPixmap(QPixmap("/Users/benjamimo1/Desktop/Ruleta/table.jpg"))
		#self.fondo.setGeometry(0, 0, 400, 400)
		self.fondo.lower()

		self.triangulo = QLabel(self)
		self.triangulo.setPixmap(QPixmap("/Users/benjamimo1/Desktop/Ruleta/triangulo.png").scaledToHeight(50))
		self.triangulo.move(200, 80)
		self.triangulo.raise_()

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