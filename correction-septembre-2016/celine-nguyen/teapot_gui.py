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
        # WINDOW'S SIZE AND POSITION
        self.setGeometry(300, 300, 300, 100)
        # WINDOW'S TITLE
        self.setWindowTitle('Let\'s create a teapot')
        
        # PARAMETERS
        # Nom de l'objet
        self.label_nom_base = QtGui.QLabel("Nom de base :")
        self.line_nom_base = QtGui.QLineEdit(parent=self)
        # Nombre de teapots
        self.label_nombre = QtGui.QLabel("Nombre :")
        self.line_nombre = QtGui.QSpinBox(parent=self)
        self.line_nombre.setMaximum(200)
        self.line_nombre.setMinimum(1)
        # Rayon du cercle
        self.label_rayon_cercle = QtGui.QLabel("Rayon du cercle :")
        self.line_rayon_cercle = QtGui.QSpinBox(parent=self)
        
        # BUTTON
        self.button = QtGui.QPushButton("Magic !", parent=self)
        self.button.pressed.connect(self.button_pressed)
        
        # LAYOUT
        layout = QtGui.QGridLayout(self)
        # Nom de base
        layout.addWidget(self.label_nom_base, 0, 0)
        layout.addWidget(self.line_nom_base, 0, 1)
        # Nombre de teapots
        layout.addWidget(self.label_nombre, 1, 0)
        layout.addWidget(self.line_nombre, 1, 1)
        # Rayon du cercle
        layout.addWidget(self.label_rayon_cercle, 2, 0)
        layout.addWidget(self.line_rayon_cercle, 2, 1)
        # Bouton
        layout.addWidget(self.button, 3, 1)

    def button_pressed(self):
        radius=self.line_rayon_cercle.value()
        count=self.line_nombre.value()
        name=self.line_nom_base.text()
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
