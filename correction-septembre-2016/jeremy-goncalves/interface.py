from PySide import QtGui
import maxhelper
import MaxPlus
import teapot

reload(maxhelper)
reload(teapot)

class _GarbageCollectorProtector(object):
    protected_widgets = list()

	

class Example(maxhelper.MaxWidget):

    def __init__(self):
		# initialisation des elements
        maxhelper.MaxWidget.__init__(self)
        self.init_ui()


    def init_ui(self):
        # Place et taille de base
        self.setGeometry(300, 300, 450, 200)
        
        # set du nom de l'objet
        self.name_label = QtGui.QLabel('Name : ')
		# preset du nom en teapot
        self.name = QtGui.QLineEdit('Teapot')

        # Radius
        self.radius_label = QtGui.QLabel('Radius :')
        self.radius = QtGui.QSpinBox()

        # nombre de teapot
        self.count_label = QtGui.QLabel('Count :')
        self.count = QtGui.QSpinBox()
        self.count.setMinimum(1)
        
        # bouton BIM
        self.button = QtGui.QPushButton("BIM")
        self.button.pressed.connect(self.button_pressed)

        # Layout de la fenetre
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.name, 0, 1)
        layout.addWidget(self.radius_label, 1, 0)
        layout.addWidget(self.radius, 1, 1)
        layout.addWidget(self.count_label, 2, 0)
        layout.addWidget(self.count, 2, 1)
        layout.addWidget(self.button, 3, 2)

        # Titre de la fenetre
        self.setWindowTitle('Creation de teapot automatique')

    def button_pressed(self):      
	
        count = int(self.count.text())
        name = self.name.text()
	radius = int(self.radius.text())
		
        teapot.teapot_circle(radius, count, name)
		
def main():

    example = Example()
    _GarbageCollectorProtector.protected_widgets.append(example)
    example.show()


if __name__ == '__main__':
    main()
