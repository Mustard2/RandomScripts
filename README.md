# RandomScripts
Collection of random scripts for Blender.
These scripts are for personal use, so it might not work for all applications.

## Instructions
Add the script in the Blender Text editor, and run them following the instructions in the comments in the first lines of the script.

## Scripts

### add_drivers

The script creates drivers on shape keys of the selected objects, using the target (the source value of he drivers) as the last selected item. The script will automatically search the shape keys of both selected objects and target object, and add drivers only when the target shape keys match the name of the shape keys in the selected objects.

**Note:** The script will automatically overwrite existing drivers on shape keys, so use it only if you want to overwrite shape keys. If not, please rename the shape keys you don't want to be linked with the driver in such a way the selected and target object shape keys are not named the same.

**Note:** This addon is only intended for creating drivers, it will not create new shape keys nor transfer shapes from one key to another: it simply use existing shape key and create drivers if the names are matching.
