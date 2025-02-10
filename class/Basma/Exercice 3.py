import pymel.core as pm

def triangle_wall():
    cube_size = 1
    spacing = 2
    row = 5
    for row in range(row):
        x_position = spacing
        for col in range (row + 1):
            x_pos = x_position + col * spacing
            y_pos = row * spacing
            z_pos = 0

            cube = pm.polyCube(w=cube_size, h=cube_size, d=cube_size)[0]
            pm.move(x_pos, y_pos, z_pos)

triangle_wall()



def triangle_wall():
    cube_size = 1
    spacing = 2
    row = 6
    for row in range(row):
        x_position = spacing* row
        for col in range (row):
            x_pos = x_position + col * -spacing
            y_pos = row * -spacing
            z_pos = 0

            cube = pm.polyCube(w=cube_size, h=cube_size, d=cube_size)[0]
            pm.move(x_pos, y_pos, z_pos)

triangle_wall()

