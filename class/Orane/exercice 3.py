#Exercice 3
import pymel.core as pm

def triangle(size, positionX=0, positionY=0, spacing=0.5):
    for i in range(0, size):
        for j in range(0, i + 1):
                cube, node = pm.polyCube()
                pm.move(cube, positionX + j * (1 + spacing), positionY + i * (1 + spacing), 0, moveXYZ=True)

triangle(10)