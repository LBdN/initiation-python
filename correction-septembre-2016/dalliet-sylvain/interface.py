from PySide import QtGui
import maxhelper
import teapot_create

__author__= "SYLVAIN DALLIET"


class _GarbageCollectorProtector(object):    
    protected_widgets = list()


class Example(maxhelper.MaxWidget):
    def __init__(self):
        # Initialise Classe Parente
        maxhelper.MaxWidget.__init__(self)
        # Initialise les elements d'interface
        self.init_ui()

    def init_ui(self):
        # Place et taille
        self.setGeometry(300, 300, 450, 200)
        
        # Name Area
        self.name_area_label = QtGui.QLabel('Base Name : ')
        self.name_area = QtGui.QLineEdit('MagicTeapot')

        # Segments Area
        self.segments_area_label = QtGui.QLabel('Nbr. Segments :')
        self.segments_area = QtGui.QSpinBox()
        self.segments_area.setMinimum(10)
        
        # Radius Area
        self.radius_area_label = QtGui.QLabel('Radius :')
        self.radius_area = QtGui.QDoubleSpinBox()
        self.radius_area.setMinimum(5.000)
        self.radius_area.setDecimals(3)
        self.radius_area.setSingleStep(0.01)
        self.radius_area.setAccelerated(True)

        # Quantity Area
        self.quantity_area_label = QtGui.QLabel('Nbr. Teapot :')
        self.quantity_area = QtGui.QSpinBox()
        self.quantity_area.setMinimum(5)

        # Circle Radius Area
        self.circle_radius_area_label = QtGui.QLabel('Circle Radius :')
        self.circle_radius_area = QtGui.QDoubleSpinBox()
        self.circle_radius_area.setMinimum(20)
        self.circle_radius_area.setDecimals(2)
        self.circle_radius_area.setSingleStep(0.01)
        self.circle_radius_area.setAccelerated(True)
        
        # Button creation
        self.button = QtGui.QPushButton("Shazam")
        self.button.pressed.connect(self.button_pressed)

        # Button fix unique name and some fun
        self.button_fix = QtGui.QPushButton("Fix unique name")
        self.button_fix.pressed.connect(self.button_fix_pressed)

        # Button fix unique name and some fun
        self.button_circle = QtGui.QPushButton("Running Circles")
        self.button_circle.pressed.connect(self.button_circle_pressed)

        # Layout
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.name_area_label, 0, 0)
        layout.addWidget(self.name_area, 0, 1)
        layout.addWidget(self.segments_area_label, 1, 0)
        layout.addWidget(self.segments_area, 1, 1)
        layout.addWidget(self.radius_area_label, 2, 0)
        layout.addWidget(self.radius_area, 2, 1)
        layout.addWidget(self.quantity_area_label, 3, 0)
        layout.addWidget(self.quantity_area, 3, 1)
        layout.addWidget(self.circle_radius_area_label, 4, 0)
        layout.addWidget(self.circle_radius_area, 4, 1)
        layout.addWidget(self.button, 5, 2)
        layout.addWidget(self.button_fix, 6, 2)
        layout.addWidget(self.button_circle, 7, 2)

        # Title
        self.setWindowTitle('The Teapot Magic Maker')


    def button_pressed(self):
        # Print a sentence using all inputs        
        print "You created {quantity} Teapot(s) with the base name \"{name}\" " \
        "with {nbr_segments} segments and " \
        "a radius of {radius_value}".format(
                quantity=self.quantity_area.text(),
                name=self.name_area.text(),
                nbr_segments=self.segments_area.text(),
                radius_value=self.radius_area.text()
            )

        # Get user values
        quantity = self.quantity_area.value()
        name = self.name_area.text()
        radius_value = self.radius_area.value()
        nbr_segments = self.segments_area.value()
        circle_radius_value = self.circle_radius_area.value()        
        
        # Loop Teapot Function
        teapot_create.loop_teapot(radius_value, nbr_segments, quantity, name)

    def button_fix_pressed(self):
        # call the fix function
        name = self.name_area.text()
        teapot_create.unique_name_fix(name)

    def button_circle_pressed(self):
        # call the circle distribution function
        name = self.name_area.text()
        circle_radius_value = self.circle_radius_area.value()
        teapot_create.teapot_circle(circle_radius_value, name)
      
def main():
    # Creation d'un widget
    example = Example()
    # Evite la suppression du widget
    _GarbageCollectorProtector.protected_widgets.append(example)
    # Affichage
    example.show()


if __name__ == '__main__':
    main()
