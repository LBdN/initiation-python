from PySide import QtGui
import maxhelper
import MaxPlus
import teapot


class _GarbageCollectorProtector(object):
    protected_widgets = list()

    
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
        self.setGeometry(300, 300, 350, 150)

        # Line
        self.line = QtGui.QLineEdit()

        # Layout
        self.nom = QtGui.QLabel('Nom de base :', self)
        self.nombre = QtGui.QLabel('Nombre :', self)
        self.rayon = QtGui.QLabel('Rayon :', self)

        self.title_edit = QtGui.QLineEdit()
        self.author_edit = QtGui.QSpinBox()
        self.review_edit = QtGui.QSpinBox()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.nom, 1, 0)
        grid.addWidget(self.title_edit, 1, 1)

        grid.addWidget(self.nombre, 2, 0)
        grid.addWidget(self.author_edit, 2, 1)

        grid.addWidget(self.rayon, 3, 0)
        grid.addWidget(self.review_edit, 3, 1)
        
        self.setLayout(grid) 
      
        # Button
        self.button = QtGui.QPushButton("HEY YA !")
        self.button.move(10, 60)
        self.button.pressed.connect(self.button_pressed)
        
        grid.addWidget(self.button, 4, 1, 2)
        
        self.show()

        # Titre
        self.setWindowTitle('TEAPOT GENERATOR')

    def button_pressed(self):
        radius = self.review_edit.value()
        count = self.author_edit.value()
        name = self.title_edit.text()
        
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
