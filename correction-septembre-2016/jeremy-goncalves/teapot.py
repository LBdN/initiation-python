import MaxPlus
import math


def create_teapot(position, rotation):

    teapot_geometry = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Teapot)
    teapot_geometry.ParameterBlock.Radius.Value = 10.0
    teapot_geometry.ParameterBlock.Segs.Value = 4

    teapot_node = MaxPlus.Factory.CreateNode(teapot_geometry)
    teapot_node.Position = MaxPlus.Point3(*position)

    rotation_quat = MaxPlus.Quat()
    rotation_quat.SetEuler(*rotation)
    teapot_node.Rotation = rotation_quat

    return teapot_node


def teapot_circle(radius, count, name):

    distribution_angle = 2 * math.pi / count

    for teapot_index in range(count):

        current_angle = distribution_angle * teapot_index
        angle_z = math.pi * (teapot_index % 2) + current_angle

        position_x = radius * math.cos(current_angle)
        position_y = radius * math.sin(current_angle)
  
        new_teapot = create_teapot([position_x, position_y, 0], [0, 0, angle_z])

        new_teapot.SetName("{teapot}{index:03d}".format(
            index=teapot_index,
            teapot=name
        ))
        new_teapot.SetWireColor(MaxPlus.Color(255 / count * teapot_index))
