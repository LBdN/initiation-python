from PySide import QtGui
import maxhelper
import teapot_generator


class _GarbageCollectorProtector(object):
	protected_widgets = list()


class Example(maxhelper.MaxWidget):

	def __init__(self):
		# Initialise Classe Parente
		maxhelper.MaxWidget.__init__(self)
		# Initialise les elements d'interface
		self.init_ui()

	def init_ui(self):
		# Place et taille
		self.setGeometry(300, 300, 250, 150)
		
		#Nom de base
		self.nom_de_base = QtGui.QLineEdit()
		self.label_nom_de_base = QtGui.QLabel("Nom de base :")
		
		#Nombre
		self.nombre = QtGui.QSpinBox()
		self.nombre.setMaximum(999999)
		self.label_nombre = QtGui.QLabel("Nombre :")
		
		#Rayon
		self.rayon = QtGui.QSpinBox()
		self.rayon.setMaximum(999999)
		self.label_rayon = QtGui.QLabel("Rayon :")
		
		# Button
		self.button = QtGui.QPushButton("BIM !", parent=self)
		self.button.pressed.connect(self.button_pressed)

		# Layout
		layout = QtGui.QGridLayout(self)
		layout.addWidget(self.label_nom_de_base, 0, 0)
		layout.addWidget(self.nom_de_base, 0, 1)
		
		layout.addWidget(self.label_nombre, 1, 0)
		layout.addWidget(self.nombre, 1, 1)
		
		layout.addWidget(self.label_rayon, 2, 0)
		layout.addWidget(self.rayon, 2, 1)
		
		layout.addWidget(self.button, 4, 1)
		
		# Titre
		self.setWindowTitle('Teapot Generator')

	def button_pressed(self):
		name = self.nom_de_base.text()
		count = self.nombre.value()
		radius = self.rayon.value()
		
		teapot_generator.teapot_circle(radius, count, name)
		

def main():
	# Creation d'un widget
	example = Example()
	# Evite la suppression du widget
	_GarbageCollectorProtector.protected_widgets.append(example)
	# Affichage
	example.show()


if __name__ == '__main__':
	main()
