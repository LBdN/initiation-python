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
        # Emplacement et taille fenetre
        self.setGeometry(300, 300, 300, 250)
                      
        # Ligne nom de base
        self.line_nom_de_base = QtGui.QLineEdit(parent=self)
        self.texte_nom_de_base = QtGui.QLabel("Nom Teapot :")
             
        # Ligne nombre
        self.line_nombre = QtGui.QSpinBox(parent=self)
        self.texte_nombre = QtGui.QLabel("Nb Teapots:")
        
        # Ligne rayon
        self.line_rayon = QtGui.QSpinBox(parent=self)
        self.texte_rayon = QtGui.QLabel("Rayon :")
                        
        # Ligne Bouton
        self.button = QtGui.QPushButton("Abracadabra !", parent=self)
        self.button.pressed.connect(self.button_pressed)

        # Ligne Titre
        self.setWindowTitle('Coucou Valentin !')

        # LAYOUT :    
        layout = QtGui.QGridLayout(self)
        
        # Emplacement nom de base
        layout.addWidget(self.texte_nom_de_base, 0, 0)
        layout.addWidget(self.line_nom_de_base, 0, 1)
        
        # Emplacement nombre
        layout.addWidget(self.texte_nombre, 1, 0)
        layout.addWidget(self.line_nombre, 1, 1)
            
        # Emplacement rayon
        layout.addWidget(self.texte_rayon, 2, 0)
        layout.addWidget(self.line_rayon, 2, 1)
        
        # Emplacement bouton
        layout.addWidget(self.button, 3, 3)
        
    def button_pressed(self):
        name = self.line_nom_de_base.text()
        count = self.line_nombre.value()
        radius = self.line_rayon.value()
        
        teapot.teapot_circle(name, count, radius)


def main():
    # Creation du widget
    teapot_tool = TeapotTool()
    # Evite la suppression du widget
    _GarbageCollectorProtector.protected_widgets.append(teapot_tool)
    # Affichage
    teapot_tool.show()
    
  
if __name__ == '__main__':
    main()
