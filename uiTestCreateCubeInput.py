import maya.cmds as cmds

def create_cube(name, length, width, height):
    cmds.polyCube(name=name, width=width, height=height, depth=length)

def create_ui():
    # Create a window
    window = cmds.window(title="Create Cube", widthHeight=(500, 150))

    # Create layout
    layout = cmds.columnLayout()

    # Create name field
    name_field = cmds.textFieldGrp(label="Name:")

    # Create length field
    length_field = cmds.floatFieldGrp(label="Length:")

    # Create width field
    width_field = cmds.floatFieldGrp(label="Width:")

    # Create height field
    height_field = cmds.floatFieldGrp(label="Height:")

    # Create create button
    cmds.button(label="Create", command=lambda *args: create_cube(cmds.textFieldGrp(name_field, query=True, text=True), 
                                                                cmds.floatFieldGrp(length_field, query=True, value1=True),
                                                                cmds.floatFieldGrp(width_field, query=True, value1=True),
                                                                cmds.floatFieldGrp(height_field, query=True, value1=True) 
                                                                ))
    # Show the window
    cmds.showWindow(window)

create_ui()