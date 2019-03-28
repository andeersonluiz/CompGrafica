
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
 
 
cores = ((0.4, 0.4, 0.4),(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), (0.0, 1.0, 1.0),(1.0, 0.0, 1.0), (1.0, 1.0, 0.0), (1.0, 1.0, 1.0), (0.0, 0.0, 0.0), (0.5, 0.0, 0.0), (0.0, 0.5, 0.0), (0.0, 0.0, 0.5),(0.0, 0.5, 0.5), (0.5, 0.0, 0.5), (0.5, 0.5, 0.0), (0.8, 0.8, 0.8))



def prismaPoligono(rBase, nBase ,altura):
    
    nLadosBase = nBase
    height = altura
    radius = rBase
    
    glBegin(GL_POLYGON)
    for vertice in range(0, nLadosBase):  
        glColor3fv(cores[vertice%len(cores)])   
        glVertex3fv([math.cos(2* math.pi * vertice/nLadosBase) * radius, -1 , math.sin(2 * math.pi * vertice/nLadosBase) * radius])
    glEnd()
    
    glBegin(GL_TRIANGLE_STRIP)        
    for vertice in range(0, nLadosBase+1):  
        glColor3fv(cores[vertice%len(cores)])         
        glVertex3fv([math.cos(2* math.pi * vertice/nLadosBase) * radius, height, math.sin(2 * math.pi * vertice/nLadosBase) * radius])    
        glVertex3fv([math.cos(2* math.pi * vertice/nLadosBase) * radius, -1 , math.sin(2 * math.pi * vertice/nLadosBase) * radius])
    glEnd()

    glBegin(GL_POLYGON)
    i=0
    for vertice in range(0, nLadosBase):     
        i+=1
        glColor3fv(cores[vertice%len(cores)])   
        glVertex3fv([math.cos(2* math.pi * vertice/nLadosBase) * radius, height, math.sin(2 * math.pi * vertice/nLadosBase) * radius])
    glEnd()
                

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    prismaPoligono(1, 100, 1)
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PRISMANBASE")
glutDisplayFunc(render)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(40,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()