# Mustard - 07/03/2021
# This script can be used to automatically create drivers on the shape keys between two objects,
# if the shape keys are named the same
#
# INSTRUCTIONS
# - Select the objects you want the drivers to be added
# - Select AS THE LAST OBJECT the target of the drivers

import bpy

def add_driver(
        source, target, prop, dataPath, index = -1):
    ''' Add driver to source prop (at index), driven by target dataPath '''

    if index != -1:
        d = source.driver_add( prop, index ).driver
    else:
        d = source.driver_add( prop ).driver
    
    # Remove old variables
    for v in d.variables:
        d.variables.remove(v)

    v = d.variables.new()
    v.name                 = 'var'
    v.targets[0].id_type   = 'KEY'
    v.targets[0].id        = target
    v.targets[0].data_path = dataPath
    
    d.type = 'AVERAGE'


def shape_keys_drivers (debug = False):
    
    if len(bpy.context.selected_objects)<2:
        print("\nError: Select at least 2 objects!")
        return False
    
    child_objects = bpy.context.selected_objects
    child_objects.remove(bpy.context.active_object)
    
    parent_object = bpy.context.active_object
    shapekey_list_string = str(parent_object.data.shape_keys.key_blocks.keys()).lower()
    
    print("\nSelected objects:")
    print("    Parent object: " + parent_object.name)
    i = 1
    for obj in child_objects:
        print("    Child object " + str(i) + ": " + obj.name)
        i = i +1
    print("\n")
    
    parent_object_sk = parent_object.data.shape_keys
    
    error_shape_keys = []
    
    if debug:
        print("ADDING DRIVERS\n")
    
    for obj in child_objects:
        
        for key in obj.data.shape_keys.key_blocks:
            
            if debug:
                print("Searching for " + key.name + " in " + obj.name)
            
            if key.name.lower().lstrip(obj.name.lower()) in shapekey_list_string and key.name != "Basis":
                
                    if debug:
                        print("Adding for " + key.name + " in " + obj.name)
                    
                    child_object_sk = obj.data.shape_keys
    
                    sk_id = 'key_blocks["' + key.name.lstrip(obj.name.lower())+ '"].value'
    
                    try:
                        add_driver(child_object_sk, parent_object_sk, sk_id, sk_id, -1)
                        if debug:
                            print("\n")
                    except:
                        print("ERROR! Can not add driver for " + key.name + " in " + obj.name + "\n")
                        error_shape_keys.append(key.name + " in " + obj.name)
            else:
                if debug:
                    print("\n")
                
    if len(error_shape_keys)>0:
        print("Some errors occurred during the script run.")
        print("The following drivers have not been added:")
        for sk in error_shape_keys:
            print(sk)
                
    return True


# Change False to True for more details during the run
shape_keys_drivers(False)