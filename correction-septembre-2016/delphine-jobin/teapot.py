import MaxPlus
import math

def create_teapot(position, rotation):
    # Create Geometry
    teapot_geometry = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Teapot)
    teapot_geometry.ParameterBlock.Radius.Value = 10.0
    teapot_geometry.ParameterBlock.Segs.Value = 4
    # Create Node
    teapot_node = MaxPlus.Factory.CreateNode(teapot_geometry)
    teapot_node.Position = MaxPlus.Point3(*position)
    # Set transform
    rotation_quat = MaxPlus.Quat()
    rotation_quat.SetEuler(*rotation)
    rotation_quat.SetEuler(*rotation)
    teapot_node.Rotation = rotation_quat
    # Return
    return teapot_node


def teapot_circle(name, count, radius):
    # Distribution Angle
    distribution_angle = 2 * math.pi / count
    # Each teapot
    for teapot_index in range(count):
        # Compute Angles
        current_angle = distribution_angle * teapot_index
        angle_z = math.pi * (teapot_index % 2) + current_angle
        # Compute position
        position_x = radius * math.cos(current_angle)
        position_y = radius * math.sin(current_angle)
        # New Teapot
        new_teapot = create_teapot([position_x, position_y, 0], [0, 0, angle_z])
        # Set Other Params
        new_teapot.SetName("{nom}_{index:03d}".format(
        index=teapot_index,
        nom=name))
        new_teapot.SetWireColor(MaxPlus.Color(255 / count * teapot_index))

