from PySide import QtGui
import maxhelper
import teapot


class _GarbageCollectorProtector(object):
    protected_widgets = list()


class Example(maxhelper.MaxWidget):
    def __init__(self):
        # Initialise Class Parent
        maxhelper.MaxWidget.__init__(self)
        # Initialise les elements de l'interface
        self.init_ui()

    def init_ui(self):
        # Place et taille Teapot
        self.setGeometry(300, 300, 450, 200)
        
        # Name objet
        self.name_label = QtGui.QLabel('Name : ')
        self.name = QtGui.QLineEdit('Teapot')

        # Radius
        self.radius_label = QtGui.QLabel('Radius :')
        self.radius = QtGui.QSpinBox()

        # Count
        self.count_label = QtGui.QLabel('Count :')
        self.count = QtGui.QSpinBox()
        self.count.setMinimum(1)
        
        # Button creation
        self.button = QtGui.QPushButton("BIM")
        self.button.pressed.connect(self.button_pressed)

        # Layout
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.name, 0, 1)
        layout.addWidget(self.radius_label, 1, 0)
        layout.addWidget(self.radius, 1, 1)
        layout.addWidget(self.count_label, 2, 0)
        layout.addWidget(self.count, 2, 1)
        layout.addWidget(self.button, 3, 2)

        # Title
        self.setWindowTitle('Teapot Create')

    def button_pressed(self):      
        # Count
        count = self.count.value()
        # Name
        name = self.name.text()
        # Radius
        radius = self.radius.value()

        # fonction
        teapot.teapot_circle(radius, count, name)
		
		
def main():
    # Creation du widget
    example = Example()
    # Evite la suppression du widget
    _GarbageCollectorProtector.protected_widgets.append(example)
    # Affichage
    example.show()


if __name__ == '__main__':
    main()
