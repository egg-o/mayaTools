import maya.cmds as cmds
import os

# The path to the folder containing the Maya files
folder_path = '/path/to/maya_files'

suffix = '_r'

# Get a list of all the Maya files in the folder
maya_files = [f for f in os.listdir(folder_path) if f.endswith('.ma')]

for maya_file in maya_files:
    # Open the Maya file
    maya_file_path = os.path.join(folder_path, maya_file)
    cmds.file(maya_file_path, open=True, force=True)

    # Delete all objects with the suffix "_r"
    objects_to_delete = cmds.ls(selection=True, objectsOnly=True, long=True)
    objects_to_delete = [x for x in objects_to_delete if x.endswith(suffix)]
    cmds.delete(objects_to_delete)

    # Save the modified Maya file
    cmds.file(save=True)


