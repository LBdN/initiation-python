from PySide import QtGui
import maxhelper
import teapot


class _GarbageCollectorProtector(object):
    protected_widgets = list()


class Round(maxhelper.MaxWidget):

    def __init__(self):
        maxhelper.MaxWidget.__init__(self)
        self.init_ui()


    def init_ui(self):
        # On donne a geometrie de l'interface
        self.setGeometry(300, 300, 450, 200)
        
        # L'input du nom
        self.name_label = QtGui.QLabel('Name : ')
        self.name = QtGui.QLineEdit('Teapot')

        # L'input du diametre
        self.diameter_label = QtGui.QLabel('Diameter :')
        self.diameter = QtGui.QSpinBox()
        self.diameter.setMinimum(5)
        
        # L'input du rayon
        self.radius_label = QtGui.QLabel('Radius :')
        self.radius = QtGui.QDoubleSpinBox()
        self.radius.setMinimum(6.000)
        self.radius.setDecimals(3)
        self.radius.setSingleStep(0.01)

        # L'input de la quantite
        self.quantity_label = QtGui.QLabel('Number :')
        self.quantity = QtGui.QSpinBox()
        self.quantity.setMinimum(8)
        
        # On cree le fameux bouton BIMM
        self.button = QtGui.QPushButton("BIMMM")
        self.button.pressed.connect(self.button_pressed)

        # On met les input dans l'interface
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.name, 0, 1)
        layout.addWidget(self.diameter_label, 1, 0)
        layout.addWidget(self.diameter, 1, 1)
        layout.addWidget(self.radius_label, 2, 0)
        layout.addWidget(self.radius, 2, 1)
        layout.addWidget(self.quantity_label, 3, 0)
        layout.addWidget(self.quantity, 3, 1)
        layout.addWidget(self.button, 4, 2)

        # On donne un titre a l'interface
        self.setWindowTitle('L\'interface des familles')

    def button_pressed(self):
        # Create teapot
        count = int(self.quantity.text())
        radius = self.radius.value()
        diameter = self.diameter.value()
        name_teapot = self.name.text()
        
        # Create number of teapot
        teapot.teapot_circle(radius, diameter, count, name)
      
def main():
    # Creation d'un widget
    round_plugin = Round()
    # On évite la suppression des widgets
    _GarbageCollectorProtector.protected_widgets.append(example)
    # On lance le plugin de création de teapots
    round_plugin.show()


if __name__ == '__main__':
    main()
