from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarArbol():
    glColor(0.7, 0.4, 0.2)
    glBegin(GL_QUADS)
    glVertex3f(-0.88, -0.8, 0)
    glVertex3f(-0.65, -0.8, 0)
    glVertex3f(-0.65, -0.15, 0)
    glVertex3f(-0.88, -0.15, 0)
    glEnd()
    glColor(0.2, 0.5, 0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.76, sin(angulo) * 0.2 - 0.1, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.71, sin(angulo) * 0.2 + 0.09, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.82, sin(angulo) * 0.2 + 0.07, 0.0)
    glEnd()

def dibujarNubes():
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        glVertex3f(cos(angulo) * 0.2 + 0.5, sin(angulo) * 0.1 + 0.8, 0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        
        glVertex3f(cos(angulo) * 0.2 + 0.6, sin(angulo) * 0.1 + 0.9, 0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        
        glVertex3f(cos(angulo) * 0.2 + 0.7, sin(angulo) * 0.1 + 0.8, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        
        glVertex3f(cos(angulo) * 0.2 - 0.3, sin(angulo) * 0.1 + 0.8, 0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        
        glVertex3f(cos(angulo) * 0.2 - 0.15, sin(angulo) * 0.1 + 0.9, 0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        glVertex3f(cos(angulo) * 0.2 + 0.7, sin(angulo) * 0.1 + 0.5, 0.0)
    glEnd()
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        glVertex3f(cos(angulo) * 0.2 + 0.77, sin(angulo) * 0.1 + 0.57, 0.0)
    glEnd()
    
def dibujarTecho():
    glColor(1, 0, 0)
    glBegin(GL_TRIANGLES)

    glVertex3f(-0.7, 0.3, 0)
    glVertex3f(0, 0.7, 0)
    glVertex3f(0.7, 0.3, 0)

    glEnd()

def dibujarPuerta():

    glColor(0.9, 0.7, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(0.2, -0.1, 0)
    glVertex3f(0.4, -0.1, 0)
    glVertex3f(0.4, -0.6, 0)
    glVertex3f(0.2, -0.6, 0)
    glEnd()

    glColor(0, 0, 0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.37, sin(angulo) * 0.02 - 0.3, 0.0)
    glEnd()

def dibujarParedes():
    
    glBegin(GL_QUADS)
    glColor(0.2, 0, 0.5)
    glVertex3f(-0.5, -0.6, 0)
    glVertex3f(0.5, -0.6, 0)
    glVertex3f(0.5, 0.3, 0)
    glVertex3f(-0.5, 0.3, 0)

    glColor(0, 0, 0)
    glVertex3f(-0.4, -0.2, 0)
    glVertex3f(0, -0.2, 0)
    glVertex3f(0, 0.2, 0)
    glVertex3f(-0.4, 0.2, 0)

    #Ventana
    glColor(0.7, 1, 1)
    glVertex3f(-0.37, -0.17, 0)
    glVertex3f(-0.2, -0.17, 0)
    glVertex3f(-0.2, -0.005, 0)
    glVertex3f(-0.37, -0.005, 0)

    glColor(0.7, 1, 1)
    glVertex3f(-0.37, 0.02, 0)
    glVertex3f(-0.2, 0.02, 0)
    glVertex3f(-0.2, 0.17, 0)
    glVertex3f(-0.37, 0.17, 0)

    glColor(0.7, 1, 1)
    glVertex3f(-0.18, 0.02, 0)
    glVertex3f(-0.03, 0.02, 0)
    glVertex3f(-0.03, 0.17, 0)
    glVertex3f(-0.18, 0.17, 0)

    glColor(0.7, 1, 1)
    glVertex3f(-0.18, -0.17, 0)
    glVertex3f(-0.03, -0.17, 0)
    glVertex3f(-0.03, -0.005, 0)
    glVertex3f(-0.18, -0.005, 0)
    
    glEnd()
    

def dibujarPasto():
    glBegin(GL_QUADS)
    glColor3f(0.1, 0.9, 0.2)
    glVertex3f(-1.0, -0.6, 0)
    glVertex3f(1.0, -0.6, 0)
    glVertex3f(1.0, -1.0, 0)
    glVertex3f(-1.0, -1.0, 0)
    glEnd()

def dibujarSol():
    
    glBegin(GL_POLYGON)
    glColor3f(1,0.9,0.2)
    for x in range(360):
        angulo = x * 3.14169 / 180.0
        glVertex3f(cos(angulo) * 0.17 - 0.8, sin(angulo) * 0.17 + 0.8, 0.0)

    glEnd()

    glColor3f(1,0.9,0.2)
    glBegin(GL_QUADS)
    glVertex3f(-0.65, 0.65, 0)
    glVertex3f(-0.63, 0.67, 0)
    glVertex3f(-0.43, 0.57, 0)
    glVertex3f(-0.45, 0.55, 0)
    
    glVertex3f(-0.62, 0.82, 0)
    glVertex3f(-0.60, 0.85, 0)
    glVertex3f(-0.40, 0.85, 0)
    glVertex3f(-0.42, 0.82, 0)

    glVertex3f(-0.85, 0.6, 0)
    glVertex3f(-0.82, 0.58, 0)
    glVertex3f(-0.82, 0.33, 0)
    glVertex3f(-0.85, 0.35, 0)

    glEnd()

def dibujar():
    #rutinas de dibujo
    dibujarPasto()
    dibujarSol()
    dibujarParedes()
    dibujarPuerta()
    dibujarTecho()
    dibujarNubes()
    dibujarArbol()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.1,0.6,1.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()