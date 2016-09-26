from PySide import QtGui
import maxhelper
import MaxPlus
import teapot

reload(teapot)

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
        self.nomEdit = QtGui.QLineEdit()
        self.nombreEdit = QtGui.QLineEdit()
        self.nombreEdit = QtGui.QSpinBox()
        self.radiusEdit = QtGui.QLineEdit()
        self.radiusEdit = QtGui.QSpinBox()
        
        # Layout
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.nom, 1, 0)
        grid.addWidget(self.nomEdit, 1, 2)

        grid.addWidget(self.nombre, 2, 0)
        grid.addWidget(self.nombreEdit, 2, 2)

        grid.addWidget(self.radius, 3, 0)
        grid.addWidget(self.radiusEdit, 3, 2)
        
        self.setLayout(grid) 
         
        self.show()
        
        # Bouton
        self.button = QtGui.QPushButton("WHO LET THE POTS OUT")
        grid.addWidget(self.button, 4, 2, 2)
        self.button.pressed.connect(self.button_pressed)



        # Titre fenetre
        self.setWindowTitle('Teapot Tool')
        

    def button_pressed(self):
        radius = int(self.radiusEdit.text())
        count = int(self.nombreEdit.text())
        name = self.nomEdit.text()
        
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