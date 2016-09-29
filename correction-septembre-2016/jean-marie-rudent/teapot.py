import MaxPlus
import math
import random

def make_teapot(rad, pos, rotation):
    # On créé la géométrie
    teapot_geometry = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Teapot)
    teapot_geometry.ParameterBlock.Radius.Value = rad
    teapot_node = MaxPlus.Factory.CreateNode(teapot_geometry)
    
    # On la positionne
    teapot_node.Position = MaxPlus.Point3(*pos)
    
	# On la fait tourner
    rotation_quat = MaxPlus.Quat()
    rotation_quat.SetEuler(*rotation)
    teapot_node.Rotation = rotation_quat
    
    #On retourne le tout
    return teapot_node

		
def teapot_circle(radius, diameter, count):
    # On définit la distribution des angles
    distribution_angle = 2 * math.pi / count
    
    #Et on est parti pour faire le cercle
    for teapot_index in range(count):
        
        # On calcule les angles
        current_angle = distribution_angle * teapot_index
        angle_z = math.pi * (teapot_index % 2) + current_angle
        
        # On leur dit quelle est leur position
        position_x = diameter * math.cos(current_angle)
        position_y = diameter * math.sin(current_angle)
        
        # On créé la teapot 
        new_teapot = make_teapot(radius, [position_x, position_y, 0], [0, 0, angle_z])
    