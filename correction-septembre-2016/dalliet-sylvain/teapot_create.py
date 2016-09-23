"""Teapot Creation Functions"""

import MaxPlus
import math
import random

__author__ = "Sylvain Dalliet"


def make_teapot(rad, seg, pos):
    # node geometry parameters
    teapot_geometry = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Teapot)
    teapot_geometry.ParameterBlock.Radius.Value = rad
    teapot_geometry.ParameterBlock.Segs.Value = seg
    
    # node creation
    teapot_node = MaxPlus.Factory.CreateNode(teapot_geometry)
    
    # Transform
    teapot_node.Position = MaxPlus.Point3(*pos)
    
    # return
    return teapot_node


def loop_teapot(radius, segment_count, teapot_count, the_name):   
    for teapot_index in range(teapot_count):
        # position offset
        teapot_pos_x = 10 * teapot_index

        # call teapot creation
        new_teapot = make_teapot(radius, segment_count, [teapot_pos_x, 0, 0])

        # Set Teapot(s) name(s) and color(s)        
        new_teapot.SetName("{teapot_name}_{index:03d}".format(
            teapot_name = the_name,
            index=teapot_index + 1
        ))
        new_teapot.SetWireColor(MaxPlus.Color(255 / teapot_count * (teapot_index + 1)))

    
def unique_name_fix(the_name):
    # fix for non unique names
    scene_objects = MaxPlus.Core.GetRootNode().Children
    checkname_list = list()
    check_name = the_name
    
    # filter the geometry and make sure we collect the one we actually need using the base name
    for obj in scene_objects:
        if check_name in obj.Name:
            checkname_list.append(obj)

    # now we process all checked objects   
    total_teapot_count = len(checkname_list)
    # rename process
    for instance_number, obj_checked in enumerate(checkname_list):
        obj_checked.SetName("{teapot_name}_{index:03d}".format(
            teapot_name = the_name,
            index=instance_number
        ))
        # color process
        obj_checked.SetWireColor(MaxPlus.Color(255 / total_teapot_count * (instance_number + 1)))
        # position process
        pos_x_offset = 50 * instance_number
        obj_checked.Position = MaxPlus.Point3(pos_x_offset, 0, 0)
        # add parameters for more fun
        # random scale
        rand_scale_value = random.randint(1,2)
        obj_checked.Scaling = MaxPlus.Point3(rand_scale_value, rand_scale_value, rand_scale_value)

        # random rotation
        rand_rotation_value = random.randint(0,360)
        rotation_quat = MaxPlus.Quat()
        rotation_quat.SetEuler(0, 0, rand_rotation_value)
        obj_checked.Rotation = rotation_quat