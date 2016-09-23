from PySide import QtGui
import maxhelper
import teapot

reload (teapot)

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
        
        # Nom des paramètres 
        self.nom_de_base = QtGui.QLabel("Nom de base :", self)
        self.nombre = QtGui.QLabel("Nombre :", self)
        self.rayon = QtGui.QLabel("Rayon du cercle :", self)
        self.radius_teapot = QtGui.QLabel("Taille :", self)
        self.segs_teapot = QtGui.QLabel("Segments :", self)
      
      
        # Line
        self.line_nom_de_base = QtGui.QLineEdit()
        self.spin_nombre = QtGui.QSpinBox()
        self.spin_rayon = QtGui.QSpinBox()
        self.spin_radius_teapot = QtGui.QSpinBox()
        self.spin_segs_teapot = QtGui.QSpinBox()
        
        
        # Button
        self.button = QtGui.QPushButton("BIM !")
        self.button.pressed.connect(self.button_pressed)
        
        # Layout
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.nom_de_base, 0, 0)
        layout.addWidget(self.line_nom_de_base, 0, 1)
        
        layout.addWidget(self.nombre, 2, 0)
        layout.addWidget(self.spin_nombre, 2, 1)
        
        layout.addWidget(self.rayon, 3, 0)
        layout.addWidget(self.spin_rayon, 3, 1)
        
        layout.addWidget(self.radius_teapot, 5, 0)
        layout.addWidget(self.spin_radius_teapot, 5, 1)
        
        layout.addWidget(self.segs_teapot, 6, 0)
        layout.addWidget(self.spin_segs_teapot, 6, 1)
        
        layout.addWidget(self.button, 8, 1)
        
              
        
        
        # Titre
        self.setWindowTitle('Teapot creator')

    def button_pressed(self):
    
        count = int(self.spin_nombre.text())
        radius = int(self.spin_rayon.text())
        radius_teapot = int(self.spin_radius_teapot.text())
        segs = int(self.spin_segs_teapot.text())
        name = self.line_nom_de_base.text()
        
        teapot.teapot_circle(radius, count, name, radius_teapot, segs)


def main():
    # Creation du widget
    teapot_tool = TeapotTool()
    # Evite la suppression du widget
    _GarbageCollectorProtector.protected_widgets.append(teapot_tool)
    # Affichage
    teapot_tool.show()


if __name__ == '__main__':
    main()