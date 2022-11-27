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
x_player1 = 0
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

w,h= 500,500
def jalan ():
    glPushMatrix()
    glBegin(GL_POLYGON) #JALAN
    glColor3f(0.412, 0.412, 0.412)
    glVertex2f(-500, 500) # A
    glVertex2f(500, 500) #B
    glVertex2f(500, -500) #C
    glVertex2f(-500, -500) #D
    glEnd()
    glPopMatrix()

def player1Car():
    glPushMatrix()
    global Pccx
    global Pccy

    if Pccx >= 330:
        Pccx = 330
    elif Pccx <= -330:
        Pccx = -330
    if Pccy >= 300:
        Pccy = 300
    if Pccy <= -30:
        Pccy = -20

    glTranslated(Pccx, Pccy, 0)
    print("Batasan Horizontal", Pccx, "Batasan Vertikal", Pccy)
    glTranslated(-30, 80, 0)
    glBegin(GL_POLYGON) #BADAN MOBIL 1
    glColor3ub(178,34,34)
    glVertex2f(20, 100) #E
    glVertex2f(40, 100) #F
    glVertex2f(80, 50) #D
    glVertex2f(80, -100) #C
    glVertex2f(-20, -100) #A
    glVertex2f(-20, 50) #B
    glEnd()

    glBegin(GL_LINES) #WHITE LINE BADAN MOBIL 1
    glColor3d(0,0,0)
    glVertex2f(80, 50) #D
    glVertex2f(50, 0)
    glVertex2f(50, 0)
    glVertex2f(50, -50)
    glVertex2f(-20, 50) #B
    glVertex2f(10, 0)
    glVertex2f(10, 0)
    glVertex2f(10, -50)
    glEnd()

    glBegin(GL_POLYGON) #BADAN MOBIL 2
    glColor3ub(178,34,34)
    glVertex2f(-20, -50) #A
    glVertex2f(80, -50) #C
    glVertex2f(130, -100) #l
    glVertex2f(130, -250) #M
    glVertex2f(80, -300) #N
    glVertex2f(-20, -300) #I
    glVertex2f(-70, -250) #H
    glVertex2f(-70, -100) #G
    glEnd()

    glBegin(GL_LINES) #WHITE LINE BADAN MOBIL 2
    glColor3d(0,0,0)
    glVertex2f(50, -50) #CABANG KANAN
    glVertex2f(100, -120)
    glVertex2f(100, -120)
    glVertex2f(100, -280)
    glVertex2f(10, -50) #CABANG KIRI
    glVertex2f(-40, -120)
    glVertex2f(-40, -120)
    glVertex2f(-40, -280)
    glEnd()

    glBegin(GL_LINES) #LINE BADAN MOBIL
    glColor3d(0,0,0)
    glVertex2f(20, 100) #E
    glVertex2f(40, 100) #F
    glVertex2f(40, 100) #F
    glVertex2f(80, 50) #D
    glVertex2f(80, 50) #D
    glVertex2f(80, -50) #C
    glVertex2f(80, -50) #C
    glVertex2f(130, -100) #l
    glVertex2f(130, -100) #l
    glVertex2f(130, -250) #M
    glVertex2f(130, -250) #M
    glVertex2f(80, -300) #N
    glVertex2f(80, -300) #N
    glVertex2f(80, -350) #Q
    glVertex2f(80, -350) #Q
    glVertex2f(-20, -350) #R
    glVertex2f(-20, -350) #R
    glVertex2f(-20, -300) #I
    glVertex2f(-20, -300) #I
    glVertex2f(-70, -250) #H
    glVertex2f(-70, -250) #H
    glVertex2f(-70, -100) #G
    glVertex2f(-70, -100) #G
    glVertex2f(-20, -50) #A
    glVertex2f(-20, -50) #A
    glVertex2f(-20, 50) #B
    glVertex2f(-20, 50) #B
    glVertex2f(20, 100) #E
    glEnd()
    
    glBegin(GL_POLYGON) #SAYAP KANAN
    glColor3ub(255,215,0)
    glVertex2f(130, -100) #l
    glVertex2f(180, -150) #P
    glVertex2f(180, -200) #O
    glVertex2f(130, -250) #M
    glEnd()

    glBegin(GL_LINES) #LINE SAYAP KANAN
    glColor3d(0,0,0)
    glVertex2f(130, -100) #l
    glVertex2f(180, -150) #P
    glVertex2f(180, -150) #P
    glVertex2f(180, -200) #O
    glVertex2f(180, -200) #O
    glVertex2f(130, -250) #M
    glVertex2f(130, -250) #M
    glVertex2f(130, -100) #l
    glEnd()

    glBegin(GL_POLYGON) #SAYAP KIRI
    glColor3ub(255,215,0)
    glVertex2f(-70, -100) #G
    glVertex2f(-120, -150) #J
    glVertex2f(-120, -200) #K
    glVertex2f(-70, -250) #H
    glEnd()

    glBegin(GL_LINES) #LINE SAYAP KIRI
    glColor3d(0,0,0)
    glVertex2f(-70, -100) #G
    glVertex2f(-120, -150) #J
    glVertex2f(-120, -150) #J
    glVertex2f(-120, -200) #K
    glVertex2f(-120, -200) #K
    glVertex2f(-70, -250) #H
    glVertex2f(-70, -250) #H
    glVertex2f(-70, -100) #G
    glEnd()

    glBegin(GL_POLYGON) #PENGENDARA
    glColor3d(0,0,0)
    glVertex2f(10, -100) #V2
    glVertex2f(50, -100) #W2
    glVertex2f(80, -150) #U2
    glVertex2f(80, -320) #Q
    glVertex2f(-20, -320) #R
    glVertex2f(-20, -150) #T2
    glEnd()

    glBegin(GL_LINES) #WHITE LINE PENGENDARA
    glColor3d(255,255,255)
    glVertex2f(80, -150) #U2
    glVertex2f(30, -200)
    glVertex2f(-20, -150) #T2
    glVertex2f(30, -200)
    glVertex2f(-20, -320) #R
    glVertex2f(30, -260)
    glVertex2f(80, -320) #Q
    glVertex2f(30, -260)
    glVertex2f(30, -200) #GARIS PUTIH PEMOTONG
    glVertex2f(30, -260)
    glEnd()

    glBegin(GL_POLYGON) #JARAK RODA ATAS KANAN
    glColor3f(0.2, 0.2, 0.2)
    glVertex2f(80, 0) #D
    glVertex2f(130, 0) #S
    glVertex2f(130, -20) #A1
    glVertex2f(80, -20) #B1
    glEnd()

    glBegin(GL_LINES) #LINE JARAK RODA ATAS KANAN
    glColor3f(0, 0, 0)
    glVertex2f(80, 0) #D
    glVertex2f(130, 0) #S
    glVertex2f(130, 0) #S
    glVertex2f(130, -20) #A1
    glVertex2f(130, -20) #A1
    glVertex2f(80, -20) #B1
    glVertex2f(80, -20) #B1
    glVertex2f(80, 0) #D
    glEnd()

    glBegin(GL_POLYGON) #RODA ATAS KANAN
    glColor3d(0,0,0)
    glVertex2f(130, 60) #J1
    glVertex2f(190, 60) #I1
    glVertex2f(190, -80) #H1
    glVertex2f(130, -80) #G1
    glEnd()

    glBegin(GL_POLYGON) #JARAK ATAS RODA KIRI
    glColor3d(0.2, 0.2, 0.2)
    glVertex2f(-20, 0) #V
    glVertex2f(-70, 0) #U
    glVertex2f(-70, -20) #W
    glVertex2f(-20, -20) #Z
    glEnd()

    glBegin(GL_LINES) #LINE JARAK ATAS RODA KIRI
    glColor3d(0, 0, 0)
    glVertex2f(-20, 0) #V
    glVertex2f(-70, 0) #U
    glVertex2f(-70, 0) #U
    glVertex2f(-70, -20) #W
    glVertex2f(-70, -20) #W
    glVertex2f(-20, -20) #Z
    glVertex2f(-20, -20) #Z
    glVertex2f(-20, 0) #V
    glEnd()

    glBegin(GL_POLYGON) #RODA ATAS KIRI
    glColor3d(0, 0, 0)
    glVertex2f(-70, 60) #J1
    glVertex2f(-130, 60) #I1
    glVertex2f(-130, -80) #H1
    glVertex2f(-70, -80) #G1
    glEnd()

    glBegin(GL_POLYGON) #JARAK RODA BAWAH TENGAH
    glColor3d(0.2, 0.2, 0.2)
    glVertex2f(-20, -320) #R
    glVertex2f(80, -320) #Q
    glVertex2f(90, -340) #L1
    glVertex2f(90, -400) #S1
    glVertex2f(80, -410) #R1
    glVertex2f(-20, -410) #Q1
    glVertex2f(-30, -400) #P1
    glVertex2f(-30, -340) #K1
    glEnd()

    glBegin(GL_LINES) #WHITE LINE JARAK RODA BAWAH TENGAH
    glColor3d(0, 0, 0)
    glVertex2f(90, -340) #L1
    glVertex2f(70, -370)
    glVertex2f(-30, -340) #K1
    glVertex2f(-10, -370)
    glVertex2f(90, -400) #S1
    glVertex2f(70, -370)
    glVertex2f(-30, -400) #P1
    glVertex2f(-10, -370)
    glVertex2f(-30, -370) #GARIS PUTIH PEMOTONG
    glVertex2f(90, -370)
    glEnd()

    glBegin(GL_POLYGON) #JARAK RODA BAWAH KANAN
    glColor3d(0.2, 0.2, 0.2)
    glVertex2f(90, -340) #L1
    glVertex2f(130, -340) #N1
    glVertex2f(130, -400) #T1
    glVertex2f(90, -400) #S1
    glEnd()

    glBegin(GL_LINES) #WHITE LINE JARAK RODA BAWAH KANAN
    glColor3d(0, 0, 0)
    glVertex2f(90, -370)
    glVertex2f(130, -370)
    glEnd()

    glBegin(GL_POLYGON) #JARAK RODA BAWAH KIRI
    glColor3d(0.2, 0.2, 0.2)
    glVertex2f(-30, -340) #K1
    glVertex2f(-70, -340) #M1
    glVertex2f(-70, -400) #O1
    glVertex2f(-30, -400) #P1
    glEnd()

    glBegin(GL_LINES) #WHITE LINE JARAK RODA BAWAH KIRI
    glColor3d(0, 0, 0)
    glVertex2f(-30, -370)
    glVertex2f(-70, -370)
    glEnd()

    glBegin(GL_LINES) #LINE JARAK RODA BAWAH
    glColor3d(0, 0, 0)
    glVertex2f(-20, -320) #R
    glVertex2f(80, -320) #Q
    glVertex2f(80, -320) #Q
    glVertex2f(90, -340) #L1
    glVertex2f(90, -340) #L1
    glVertex2f(130, -340) #N1
    glVertex2f(130, -340) #N1
    glVertex2f(130, -400) #T1
    glVertex2f(130, -400) #T1
    glVertex2f(90, -400) #S1
    glVertex2f(90, -400) #S1
    glVertex2f(80, -410) #R1
    glVertex2f(80, -410) #R1
    glVertex2f(-20, -410) #Q1
    glVertex2f(-20, -410) #Q1
    glVertex2f(-30, -400) #P1
    glVertex2f(-30, -400) #P1
    glVertex2f(-70, -400) #O1
    glVertex2f(-70, -400) #O1
    glVertex2f(-70, -340) #M1
    glVertex2f(-70, -340) #M1
    glVertex2f(-30, -340) #K1
    glVertex2f(-30, -340) #K1
    glVertex2f(-20, -320) #R
    glEnd()

    glBegin(GL_POLYGON) #RODA BAWAH KANAN
    glColor3d(0,0,0)
    glVertex2f(130, -300) #A1
    glVertex2f(190, -300) #B1
    glVertex2f(190, -440) #E1
    glVertex2f(130, -440) #D1
    glEnd()

    glBegin(GL_POLYGON) #RODA BAWAH KIRI
    glColor3d(0,0,0)
    glVertex2f(-70, -300) #U1
    glVertex2f(-130, -300) #Z1
    glVertex2f(-130, -440) #W1
    glVertex2f(-70, -440) #V1
    glEnd()

    glBegin(GL_POLYGON) #sAYAP BELAKANG 1
    glColor3d(0,0,0)
    glVertex2f(-20, -410) #Q1
    glVertex2f(80, -410) #R1
    glVertex2f(80, -460) #G2
    glVertex2f(-20, -460) #F2
    glEnd()

    glBegin(GL_POLYGON) #sAYAP BELAKANG 2
    glColor3d(0,0,0)
    glVertex2f(80, -430) #G2
    glVertex2f(190, -500) #J2
    glVertex2f(190, -550) #Q2
    glVertex2f(170, -530) #R2
    glVertex2f(-110, -530) #K2
    glVertex2f(-130, -550) #I2
    glVertex2f(-130, -500) #H2
    glVertex2f(-20, -430) #Q1
    glEnd()

    glBegin(GL_POLYGON) #sAYAP BELAKANG 3
    glColor3ub(178,34,34)
    glVertex2f(-80, -530) #S2
    glVertex2f(-50, -510) #Z2
    glVertex2f(110, -510) #A3
    glVertex2f(140, -530) #L2
    glVertex2f(110, -550) #M2
    glVertex2f(-50, -550) #P2
    glEnd()

    glBegin(GL_LINES) #LINE sAYAP BELAKANG 3
    glColor3d(0,0,0)
    glVertex2f(-80, -530) #S2
    glVertex2f(-50, -510) #Z2
    glVertex2f(-50, -510) #Z2
    glVertex2f(110, -510) #A3
    glVertex2f(110, -510) #A3
    glVertex2f(140, -530) #L2
    glVertex2f(140, -530) #L2
    glVertex2f(110, -550) #M2
    glVertex2f(110, -550) #M2
    glVertex2f(-50, -550) #P2
    glVertex2f(-50, -550) #P2
    glVertex2f(-80, -530) #S2
    glVertex2f(-80, -530) #S2 (t3)
    glVertex2f(140, -530) #L2 (t3)
    glEnd()

    glBegin(GL_LINES) #WHITE LINE sAYAP BELAKANG
    glColor3d(255,255,255)
    glVertex2f(-50, -510) #Z2 (1)
    glVertex2f(10, -460)
    glVertex2f(10, -460)
    glVertex2f(10, -410)
    glVertex2f(-50, -510) #Z2 (2)
    glVertex2f(-80, -480)
    glVertex2f(110, -510) #A3 (1)
    glVertex2f(50, -460)
    glVertex2f(50, -460)
    glVertex2f(50, -410)
    glVertex2f(110, -510) #A3 (2)
    glVertex2f(140, -480)
    glEnd()

    glPopMatrix()

def gerak(key,x,y):
    global Pccx
    global Pccy
    if key == GLUT_KEY_RIGHT:
        Pccx += 20
    elif key == GLUT_KEY_LEFT :
        Pccx -= 20
    elif key == GLUT_KEY_DOWN:
        Pccy -= 20
    elif key == GLUT_KEY_UP:
        Pccy += 20

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-500, 500, -500, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    jalan()
    player1Car()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutSpecialFunc(gerak)
glutIdleFunc(showScreen)
glutMainLoop()