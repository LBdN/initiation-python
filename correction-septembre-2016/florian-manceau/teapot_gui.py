from PySide import QtGui
import maxhelper
import MaxPlus
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
        layout = QtGui.QGridLayout(self)
  
        # Line
        self.lineedit_name = QtGui.QLineEdit("Teapot_")
        self.label_name = QtGui.QLabel("Nom de base :")
        layout.addWidget(self.label_name, 0, 0)
        layout.addWidget(self.lineedit_name, 0, 1)
        
        # Rayon teapot
        self.spinner_radius = QtGui.QSpinBox()
        self.label_radius = QtGui.QLabel("Rayon :")
        layout.addWidget(self.label_radius, 1, 0)
        layout.addWidget(self.spinner_radius, 1, 1)
        
        # Segments teapot
        self.spinner_segment = QtGui.QSpinBox()
        self.label_segment = QtGui.QLabel("Segments :")
        layout.addWidget(self.label_segment, 2, 0)
        layout.addWidget(self.spinner_segment, 2, 1)
        
        # nombre teapot
        self.spinner_count = QtGui.QSpinBox()
        self.label_count = QtGui.QLabel("Nombres :")
        layout.addWidget(self.label_count, 3, 0)
        layout.addWidget(self.spinner_count, 3, 1)
        
        # Rayon cercle
        self.spinner_circle_radius = QtGui.QSpinBox()
        self.label_circle_radius = QtGui.QLabel("Rayon cercle :")
        layout.addWidget(self.label_circle_radius, 4, 0)
        layout.addWidget(self.spinner_circle_radius, 4, 1)
        
        # Button
        self.button = QtGui.QPushButton("Create")
        self.button.pressed.connect(self.button_pressed)
        layout.addWidget(self.button, 5, 2)        

        # Titre
        self.setWindowTitle('Teapot Tool')
        
    def button_pressed(self):
        # Create geometry
        radius = self.spinner_radius.value()
        segment = self.spinner_segment.value()
        nombre = self.spinner_count.value()
        rayon_cercle = self.spinner_circle_radius.value()
        name = self.lineedit_name.text()
        
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
