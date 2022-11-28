import random
import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

Pccx = 0
Pccy = 0 

play = False
y_rintangan = 50 # digunakan untuk pergerakan rintangan ke bawah
tr = 500
cek_lev = 1

# PLAYER 1
x_player1 = 120
y_player1 = 0
grid_player1 = [100,300,0,500] #Untuk collission
# Logika player 1
y = 500
kecepatan = 10
cek_point = 30
cek_y = 50
cek_kecepatan = 5000
#collison
crash_wal_player1 = False # True ketika menabrak
# score
score_player1 = 0
fix_score_player1 = 0
# rintangan
x_r_player1 = random.randrange(150,250,10)#10 ini dari inputan keyboard dari mobil harus sama
tingkatan1 = 1 # for level counting


#obejeck jalan ()
def jalan ():
    glPushMatrix()
    glBegin(GL_POLYGON)
    # glColor3f(0,0,0)
    glVertex2f(120, 500) # A
    glVertex2f(300, 500) #B
    glVertex2f(300, 0) #C
    glVertex2f(120, 0) #D
    glEnd() #jalan buat player 1

    glBegin(GL_POLYGON)
    # glColor3f(0,0,0)
    glVertex2f(420, 500) # A
    glVertex2f(600, 500) #B
    glVertex2f(600, 0) #C
    glVertex2f(420, 0) #D
    glEnd() #jalan buat player 2 ==> dibuat 1 fungsi jalan seharusnya 
                                    #interface dulu

    glLineWidth(10)
    glColor3ub(255, 255, 255)
    glBegin(GL_LINES)
    glVertex2f(115, 500)
    glVertex2f(115, 0)
    glEnd() #tepi jalan plyaer 1 sisi kiri (Buat fungsi sendiri)

    glLineWidth(10)
    glColor3ub(255, 255, 255)
    glBegin(GL_LINES)
    glVertex2f(305, 500)
    glVertex2f(305, 0)
    glEnd() # tepi jalan player 1 sisi kanan (buat fungsi sendiri)

    glLineWidth(10)
    glColor3ub(255, 255, 255)
    glBegin(GL_LINES)
    glVertex2f(605, 500)
    glVertex2f(605, 0)
    glEnd() # tepi jalan player 2 sisi kiri (Buat fungsi sendiri)

    glLineWidth(10)
    glColor3ub(255, 255, 255)
    glBegin(GL_LINES)
    glVertex2f(420, 500)
    glVertex2f(420, 0)
    glEnd() # tepi jln player 2 sisi kanan (buat fungsi sendiri)

    glColor3f(0,0,204 )
    glLineWidth(30)
    glBegin(GL_LINES)
    glVertex2f(210, 500)
    glVertex2f(210, 0)
    glEnd() #garis tengah (Playaer 1) ==> buat fungsi sendiri (def garis tengah)

    glColor3f(0,0,204 )
    glLineWidth(30)
    glBegin(GL_LINES)
    glVertex2f(510, 500)
    glVertex2f(510, 0)
    glEnd() #garis tengah (Playaer 2)

    glColor3f(255, 255, 102)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(208, 100)
    glVertex2f(208, 50)
    glEnd() #garis putus 1 (player 1) ==> def sendiri nanti

    glColor3f(255, 255, 102)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(208, 170)
    glVertex2f(208, 120)
    glEnd() #garis putus 2 (player 1) ==> def sendiri nanti

    
    glColor3f(255, 255, 102)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(208, 190)
    glVertex2f(208, 240)
    glEnd() #garis putus 3 (player 1) ==> def sendiri nanti

    glColor3f(255, 255, 102)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(208, 210)
    glVertex2f(208, 240)
    glEnd() #garis putus 4 (player 1) ==> def sendiri nanti

    glColor3f(255, 255, 102)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(208, 260)
    glVertex2f(208, 310)
    glEnd() #garis putus 5 (player 1) ==> def sendiri nanti

    glColor3f(255, 255, 102)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(208, 330)
    glVertex2f(208, 380)
    glEnd() #garis putus 6 (player 1) ==> def sendiri nanti

    glColor3f(255, 255, 102)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(208, 400)
    glVertex2f(208, 450)
    glEnd() #garis putus 7 (player 1) ==> def sendiri nanti

    glColor3f(255, 255, 102)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(208, 470)
    glVertex2f(208, 500)
    glEnd() #garis putus 7 (player 1) ==> def sendiri nanti
    glPopMatrix()

#Objeck Mobil
def Mobil():
    glPushMatrix()
    global Pccx
    global Pccy
    glTranslated(Pccx,0,0)
    glBegin(GL_POLYGON)
    glColor3d(0, 0,225)
    glVertex2f(130, 0) # A
    glVertex2f(130,50) #B
    glVertex2f(180,50 ) #E
    glVertex2f(180,0) #F
    glEnd()

    glBegin(GL_POLYGON)
    glColor3d(0, 0, 225)
    glVertex2f(130,50) #B
    glVertex2f(140.50,80.06) #C
    glVertex2f(170.50,80.06) #D
    glVertex2f(180,50 ) #E
    glEnd()

    #lampu kiri
    glPointSize(5)
    glColor3d(255,255,0)
    glBegin(GL_POINTS)
    glVertex2f(145, 77)
    glEnd()

    #lampu kanan
    glPointSize(5)
    glColor3d(255,255,0)
    glBegin(GL_POINTS)
    glVertex2f(167, 77)
    glEnd()

    #hiasan
    glColor3d(255,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(137, 5) #a
    glVertex2f(137, 10) #b
    glVertex2f(170, 10) #c
    glVertex2f(170, 5) #d
    glEnd()

    glColor3d(30,10,110)
    glBegin(GL_POLYGON)
    glVertex2f(150, 13) #a
    glColor3d(100,0,255)
    glVertex2f(150, 40) #b
    glColor3d(0,0,255)
    glVertex2f(155, 40) #c
    glVertex2f(155, 13) #d
    glEnd()
    glPopMatrix()

def gerak(key,x,y):
    global Pccx
    global Pccy
    if key == GLUT_KEY_RIGHT:
        Pccx += 100
    elif key == GLUT_KEY_LEFT :
        Pccx -= 100
    elif key == GLUT_KEY_DOWN:
        Pccy -=100

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 650,0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    jalan()
    Mobil()
    glutSwapBuffers()

def Main():
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 500)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("OpenGL Coding Practice")
    glutDisplayFunc(showScreen)
    glutSpecialFunc(gerak)
    glutIdleFunc(showScreen)
    glutMainLoop()

Main()