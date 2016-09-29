from PySide import QtGui
import maxhelper
import teapot


class _GarbageCollectorProtector(object):
    protected_widgets = list()


class TeapotTool(maxhelper.MaxWidget):
    def __init__(self):
        # Initialise Classe Parente
        maxhelper.MaxWidget.__init__(self)
        # Initialise les elements d'interface
        self.init_ui()

    def init_ui(self):
        # Place et taille
        self.setGeometry(300, 300, 250, 150)
        
        # TItre des lignes
        self.nom = QtGui.QLabel('Nom')
        self.nombre = QtGui.QLabel('Nombre')
        self.radius = QtGui.QLabel('Radius')
        
        # Lignes et Spinbox
        self.nom_edit = QtGui.QLineEdit()
        self.nombre_edit = QtGui.QSpinBox()
        self.radius_edit = QtGui.QSpinBox()
        
        # Layout
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.nom, 1, 0)
        grid.addWidget(self.nom_edit, 1, 2)

        grid.addWidget(self.nombre, 2, 0)
        grid.addWidget(self.nombre_edit, 2, 2)

        grid.addWidget(self.radius, 3, 0)
        grid.addWidget(self.radius_edit, 3, 2)
        
        self.setLayout(grid) 
        
        # Bouton
        self.button = QtGui.QPushButton("WHO LET THE POTS OUT")
        grid.addWidget(self.button, 4, 2, 2)
        self.button.pressed.connect(self.button_pressed)

        # Titre fenetre
        self.setWindowTitle('Teapot Tool')
        

    def button_pressed(self):
        radius = self.radius_edit.value()
        count = self.nombre_edit.value()
        name = self.nom_edit.text()
        
        teapot.teapot_circle(radius, count, name)


def main():
    # Creation du widget
    teapot_tool = TeapotTool()
    # Evite la suppression du widget
    _GarbageCollectorProtector.protected_widgets.append(teapot_tool)
    # Affichage
    teapot_tool.show()


if __name__ == '__main__':
    main()
