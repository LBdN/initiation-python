import math
import MaxPlus


def create_teapot(radius, segment, position, rotation):
    # Create Geometry
    teapot_geometry = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Teapot)
    teapot_geometry.ParameterBlock.Radius.Value = radius
    teapot_geometry.ParameterBlock.Segs.Value = segment

    # Create Node
    teapot_node = MaxPlus.Factory.CreateNode(teapot_geometry)
    teapot_node.Position = MaxPlus.Point3(*position)
    
    # Set transform
    rotation_quat = MaxPlus.Quat()
    rotation_quat.SetEuler(*rotation)
    teapot_node.Rotation = rotation_quat
    
    # Return
    return teapot_node


def teapot_circle(radius, segment, rayon_cercle, nombre, name):
    # Distribution Angle
    distribution_angle = 2 * math.pi / nombre
    # Each teapot
    for teapot_index in range(nombre):
        # Compute Angles
        current_angle = distribution_angle * teapot_index
        angle_z = math.pi * (teapot_index % 2) + current_angle
        # Compute position
        position_x = rayon_cercle * math.cos(current_angle)
        position_y = rayon_cercle * math.sin(current_angle)
        # New Teapot
        new_teapot = create_teapot(radius, segment, [position_x, position_y, 0], [0, 0, angle_z])
       
        # Set Other Params
        new_teapot.SetName("{teapot_name}_{index:03d}".format(
            teapot_name=name,
            index=teapot_index
        ))
        new_teapot.SetWireColor(MaxPlus.Color(255 / nombre * teapot_index))
