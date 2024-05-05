from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

#ANGULOS MINIMOS Y MAXIMOS DE CADA SERVO
#pie izquierdo
min_0= 50
max_0= 170

#tobillo izquierdo
min_1=20
max_1=180

#rodilla izquierda
min_2=0
max_2=180

#muslo izquierdo
min_3=50
max_3=180

#cadera izquierda
min_4=90
max_4=160

#mano iquierda
min_5=30
max_5=160

#codo izquierda
min_6=0
max_6=90

#hombro iquierda
min_7=0
max_7=180

#pie derecho
min_8= 50
max_8= 170

#tobillo derecho
min_9=20
max_9=180

#rodilla derecho
min_10=0
max_10=180

#muslo derecho
min_11=50
max_11=180

#cadera derecho
min_12=90
max_12=160

#mano derecho
min_13=30
max_13=160

#codo derecho
min_14=40
max_14=180

#hombro derecho
min_15=0
max_15=180

def set_mode():  #POSISION INICIAL, TODOS LOS SERVOS EN EL CENTRO
 kit.servo[0].angle = 120 #pie izquierdo
 kit.servo[1].angle = 90 #tobillo izquierdo
 kit.servo[2].angle = 70 #rodilla izquierda
 kit.servo[3].angle = 90 #muslo izquierdo
 kit.servo[4].angle = 120 #cadera izquierda
 kit.servo[5].angle = 90 #mano izquierda
 kit.servo[6].angle = 30 #codo izquierdo
 kit.servo[7].angle = 170 #hombro izquerdo
 kit.servo[8].angle = 120 #pie derecho
 kit.servo[9].angle = 150  #tobillo derecho
 kit.servo[10].angle = 130 #rodilla derecha
 kit.servo[11].angle = 90 #muslo derecho
 kit.servo[12].angle = 120 #cadera derecha
 kit.servo[13].angle = 120 #mano derecha
 kit.servo[14].angle = 100 # codo derecho
 kit.servo[15].angle = 70 #hombro derecho

def ask():
    servo= int(input("Que servo quieres mover?"))
    angle= int(input("A que angulacion?"))
    kit.servo[servo].angle= angle
    
def clear():
    kit.servo[0].angle = None
    kit.servo[1].angle = None
    kit.servo[2].angle = None
    kit.servo[3].angle = None
    kit.servo[4].angle = None
    kit.servo[5].angle = None
    kit.servo[6].angle = None
    kit.servo[7].angle = None
    kit.servo[8].angle = None
    kit.servo[9].angle = None
    kit.servo[10].angle = None
    kit.servo[11].angle = None
    kit.servo[12].angle = None
    kit.servo[13].angle = None
    kit.servo[14].angle = None
    kit.servo[15].angle = None
    
def off():
    set_mode()
    kit.servo[1].angle = 20 #pie izquierdo
    kit.servo[9].angle = 20 #pie derecho
    clear()
