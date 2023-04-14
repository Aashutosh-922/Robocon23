import RPi.GPIO as GPIO
import pygame

#XBOX One 
#Rabbit Bot

pygame.init()
pygame.joystick.init()
try:
    joyStick = pygame.joystick.Joystick(0)
    joyStick.init()
except:
    pass
DIR1 = 22
DIR2 = 31
DIR3 = 33
DIR4 = 18
PWM_PIN_1 = 32
PWM_PIN_2 = 36
PWM_PIN_3 = 16  # 38
PWM_PIN_4 = 12  # 40

URD = 7
LRD = 13

UR_PWM = 15
LR_PWM = 29

SHACT = 19  # gear claw
SH_PWM = 35 

CLAW = 21  # claw mechanism
CLAW_PWM = 23

CSM = 24  # ring pushing
CSM_PWM = 26 #spi


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(PWM_PIN_1, GPIO.OUT)
GPIO.setup(PWM_PIN_2, GPIO.OUT)
GPIO.setup(PWM_PIN_3, GPIO.OUT)
GPIO.setup(PWM_PIN_4, GPIO.OUT)

GPIO.setup(SHACT, GPIO.OUT)
GPIO.setup(SH_PWM, GPIO.OUT)


GPIO.setup(URD, GPIO.OUT)
GPIO.setup(LRD, GPIO.OUT)
GPIO.setup(UR_PWM, GPIO.OUT)
GPIO.setup(LR_PWM, GPIO.OUT)

GPIO.setup(CLAW, GPIO.OUT)
GPIO.setup(CLAW_PWM, GPIO.OUT)

GPIO.setup(CSM, GPIO.OUT)
GPIO.setup(CSM_PWM, GPIO.OUT)





SPD1 = GPIO.PWM(PWM_PIN_1, 1000)
SPD2 = GPIO.PWM(PWM_PIN_2, 1000)
SPD3 = GPIO.PWM(PWM_PIN_3, 1000)
SPD4 = GPIO.PWM(PWM_PIN_4, 1000)

SPD_UR = GPIO.PWM(UR_PWM, 1000)
SPD_LR = GPIO.PWM(LR_PWM, 1000)

SPD_CLAW = GPIO.PWM(CLAW_PWM, 1000)
SPD_SHACT = GPIO.PWM(SH_PWM, 1000)
SPD_CSM = GPIO.PWM(CSM_PWM, 1000)


SPD1.start(0)
SPD2.start(0)
SPD3.start(0)
SPD4.start(0)

SPD_UR.start(0)
SPD_LR.start(0)

SPD_CLAW.start(0)
SPD_CSM.start(0)
SPD_SHACT.start(0)

# high cw low acw
def F(speed):  # forward
    GPIO.output(DIR1, GPIO.LOW)    # S
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.LOW)
    GPIO.output(DIR4, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)


def B(speed):  # backward
    GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.HIGH)
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)


def L(speed):  # left
    GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.HIGH)
    GPIO.output(DIR4, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)


def R(speed):  # right
    GPIO.output(DIR1, GPIO.LOW)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.LOW)
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)


def FLD(speed):  # forward left diagonal
    GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.HIGH)
    GPIO.output(DIR4, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(0)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(0)
    SPD4.ChangeDutyCycle(speed)


def FRD(speed):  # forward right diagonal
    GPIO.output(DIR1, GPIO.LOW)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.LOW)
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(0)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(0)


def BLD(speed):  # backward left diagonal
    GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.HIGH)
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(0)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(0)
    SPD4.ChangeDutyCycle(speed)


def FRD(speed):  # backward right diagonal
    GPIO.output(DIR1, GPIO.LOW)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.LOW)
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(0)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(0)


def STOP():
    GPIO.output(DIR1, GPIO.HIGH)
    GPIO.output(DIR2, GPIO.HIGH)
    GPIO.output(DIR3, GPIO.HIGH)
    GPIO.output(DIR4, GPIO.HIGH)

    GPIO.output(URD, GPIO.HIGH)
    GPIO.output(LRD, GPIO.HIGH)

    SPD1.ChangeDutyCycle(0)
    SPD2.ChangeDutyCycle(0)
    SPD3.ChangeDutyCycle(0)
    SPD4.ChangeDutyCycle(0)
    SPD_UR.ChangeDutyCycle(0)
    SPD_LR.ChangeDutyCycle(0)

# MSPEED = 0
# PWM = 75
# MAXSPEED = round((PWM/255) * 100)
# PWMSPD = [40, 40, 50, 50]
# # PWMPTRCNT = 3
# PWMPTR = 0

# PWMCHNG = False

def THROW(speed):
      GPIO.output(URD, GPIO.LOW)    # AC
      GPIO.output(LRD, GPIO.HIGH)    # C
      SPD_UR.ChangeDutyCycle(speed)
      SPD_LR.ChangeDutyCycle(speed)
      print(speed)

MSPEED = 0
PWM = 75
MAXSPEED = round((PWM/255) * 100)

PWMPTR = 0
startThrow = False
PWMCHNG = False
btn = None


while True:
    # mpu()
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            x = round(joyStick.get_axis(0)*100)      #left joystick   0,1, 4 =right trigger
            y = -round(joyStick.get_axis(1)*100)                             
            spd = round(joyStick.get_axis(4)*100)/2 + 50
            z = joyStick.get_hat(0)
            # print(x)
            # print(y)
            print(spd)
            #print(z)
            
            if (spd>2):
                if (x>-20 and x<20) and (y>-20 and y<20):
                    STOP()
                    print("Stop")
                elif (x>70) and (y>-70 and y<70):
                    R(spd)
                    print("Right")
                elif (x<-70) and (y>-70 and y<70):
                    L(spd)
                    print("Left")
                elif (y>70) and (x>-70 and x<70):
                    F(spd)
                    print("Forward")
                elif (y<-70) and (x>-70 and x<70):
                    B(spd)
                    print("Backward")
                else:
                    STOP()
                    print("Stop 2")
            else:
                STOP()
                print("Stop 3")
        
        elif event.type == pygame.JOYBUTTONDOWN:
            btn = event.button
        elif event.type == pygame.JOYBUTTONUP:
            btn = event.button + 20
        
        elif event.type == pygame.JOYHATMOTION:
            btn= joyStick.get_hat(0)
            print("pressed")
            print(btn)
        


        if btn != None:
            if btn == 6: #L1 #throwstart  #leftbumper
                startThrow = True
                PWMPTR = 0
        
            elif btn == 1: #O  #throwstop  #B
                startThrow = False
                PWMPTR = 0
            
            elif btn == 7:  #gearsclaw #rightbumper
                print("SHACT")
                GPIO.output(SHACT, GPIO.LOW)
                SPD_SHACT.ChangeDutyCycle(50)

                #time.sleep(1)
                #GPIO.output(SHACT, GPIO.HIGH)

            elif btn == 27:
                GPIO.output(SHACT, GPIO.HIGH)

            
            elif btn == 4:#triangle claw down  #Y
                GPIO.output(CLAW, GPIO.HIGH)
                SPD_CLAW.ChangeDutyCycle() 

            elif btn == 0: #cross Claw up  #A
                GPIO.outout(CLAW, GPIO.LOW)
                SPD_CLAW.ChangeDutyCycle(spd)
            
            elif btn == 24 or btn == 20:
                GPIO.output(CLAW, GPIO.HIGH)
                #GPIO.output(CLAW, GPIO.LOW)
                SPD_CLAW.ChangeDutyCycle(0)
            
            elif btn == 3:    #servo pushing  #X
                angle=90
                duty= (angle/18)+3
                SPD_CSM.ChangeDutyCycle(duty)

            elif btn == 23:
                angle=0
                duty= (angle/18)+3
                SPD_CSM.ChangeDutyCycle(duty)

            elif btn == (1,0):     #lx1
                MSPEED = 50
                startThrow = True
                print("trajectory1")
            
            elif btn == (-1,0):  #Rx1
                
                MSPEED = 40
                startThrow = True
                print("trajectory2")


            elif btn == (0,1): #top^
                
                MSPEED = 30
                startThrow = True
                print("trajectory3") 


            elif btn == (0,-1): #bottom^
                MSPEED = 20
                startThrow = True
                print("trajectory4")

            
            

             

    if(startThrow) :
        if(MSPEED < MAXSPEED) :
                #THROW(MAXSPEED)
            MSPEED += 1
                  
    

    elif not startThrow and MSPEED > 0 :
        MSPEED -= 1
    
    THROW(MSPEED)