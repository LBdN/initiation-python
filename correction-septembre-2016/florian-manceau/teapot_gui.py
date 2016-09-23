from PySide import QtGui
import maxhelper
import MaxPlus
import teapot


reload(maxhelper)
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
        layout = QtGui.QGridLayout(self)
  
        # Line
        self.name = QtGui.QLineEdit("Teapot_")
        self.label_name = QtGui.QLabel("Nom de base :")
        layout.addWidget(self.label_name, 0, 0)        
        layout.addWidget(self.name, 0, 1)   
        
        # Rayon teapot
        self.radius = QtGui.QSpinBox()
        self.label_radius = QtGui.QLabel("Rayon :")     
        layout.addWidget(self.label_radius, 1, 0)        
        layout.addWidget(self.radius, 1, 1)
        
        # Segments teapot
        self.segment = QtGui.QSpinBox()
        self.label_segment = QtGui.QLabel("Segments :")   
        layout.addWidget(self.label_segment, 2, 0)        
        layout.addWidget(self.segment, 2, 1)
        
        # nombre teapot
        self.number = QtGui.QSpinBox()
        self.label_number = QtGui.QLabel("Nombres :")        
        layout.addWidget(self.label_number, 3, 0)        
        layout.addWidget(self.number, 3, 1)     
        
        # Rayon cercle
        self.radius_circle = QtGui.QSpinBox()
        self.label_circle = QtGui.QLabel("Rayon cercle :")        
        layout.addWidget(self.label_circle, 4, 0)        
        layout.addWidget(self.radius_circle, 4, 1)
        
        # Button
        self.button = QtGui.QPushButton("Create")
        self.button.pressed.connect(self.button_pressed)
        layout.addWidget(self.button, 5, 2)        

        # Titre
        self.setWindowTitle('Teapot Tool')
        
        
    def button_pressed(self):
        # Create geometry
        radius = int(self.radius.text())
        segment = int(self.segment.text())
        nombre = int(self.number.text())
        rayon_cercle = int(self.radius_circle.text())   
        name = self.name.text()
        
        # Create teapot Circle 
        teapot.teapot_circle(radius, segment, rayon_cercle, nombre, name)


def main():
    # Creation d'un widget
    teapot_tool = TeapotTool()
    # Evite la suppression du widget
    _GarbageCollectorProtector.protected_widgets.append(teapot_tool)
    # Affichage
    teapot_tool.show()


if __name__ == '__main__':
    main()
