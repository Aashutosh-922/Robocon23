import RPi.GPIO as GPIO
import pygame
import time
import math
#from mpu6050 import mpu6050

# Initialize MPU6050
#sensor = mpu6050(0x68)

pygame.init()
pygame.joystick.init()
try:
    joyStick =pygame.joystick.Joystick(0)
    joyStick.init()
except:
    print("error")
    pass
 

DIR1 = 22
DIR2 = 31
DIR3 = 33
DIR4 = 18
PWM_PIN_1 = 32
PWM_PIN_2 = 36
PWM_PIN_3 = 16    #38
PWM_PIN_4 = 12 #40


URD = 7
LRD = 13

UR_PWM = 15
LR_PWM = 26   #spi #29

SHACT = 19 #pneumatics 

CLAW = 21  #claw mechanism
CLAW_PWM = 23

PUSH = 24  #ring pushing pnactuator

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

GPIO.setup(URD, GPIO.OUT)
GPIO.setup(LRD, GPIO.OUT)
GPIO.setup(UR_PWM, GPIO.OUT)
GPIO.setup(LR_PWM, GPIO.OUT)

GPIO.setup(CLAW, GPIO.OUT)
GPIO.setup(CLAW_PWM, GPIO.OUT)

GPIO.setup(PUSH, GPIO.OUT)



SPD1 = GPIO.PWM(PWM_PIN_1, 1000)
SPD2 = GPIO.PWM(PWM_PIN_2, 1000)
SPD3 = GPIO.PWM(PWM_PIN_3, 1000)
SPD4 = GPIO.PWM(PWM_PIN_4, 1000)

SPD_UR= GPIO.PWM(UR_PWM, 1000)
SPD_LR= GPIO.PWM(LR_PWM, 1000)

SPD_CLAW = GPIO.PWM(CLAW_PWM, 1000)
#SPD_CSM =  GPIO.PWM(CSM, 1000)

SPD1.start(0)
SPD2.start(0)
SPD3.start(0)
SPD4.start(0)

SPD_UR.start(0)
SPD_LR.start(0)

SPD_CLAW.start(0)
#SPD_CSM.start(0)

# MSPEED = 0
# PWM = 75
# MAXSPEED = round((PWM/255) * 100)
# PWMSPD = [40, 40, 50, 50]
# # PWMPTRCNT = 3
# PWMPTR = 0

# PWMCHNG = False


# def set_motor_speed(direction,speed):

#     if direction == 'forward':
#         SPD1.ChangeDutyCycle(speed)
#         SPD2.ChangeDutyCycle(speed)
#         SPD3.ChangeDutyCycle(speed)
#         SPD4.ChangeDutyCycle(speed)
#     elif direction == 'backward':
#         SPD1.ChangeDutyCycle(speed)
#         SPD2.ChangeDutyCycle(speed)
#         SPD3.ChangeDutyCycle(speed)
#         SPD4.ChangeDutyCycle(speed)
#     elif direction == 'left':
#         SPD1.ChangeDutyCycle(speed)
#         SPD2.ChangeDutyCycle(0)
#         SPD3.ChangeDutyCycle(speed)
#         SPD4.ChangeDutyCycle(0)
#     elif direction == 'right':
#         SPD1.ChangeDutyCycle(0)
#         SPD2.ChangeDutyCycle(speed)
#         SPD3.ChangeDutyCycle(0)
#         SPD4.ChangeDutyCycle(speed)
#     else:
#         SPD1.ChangeDutyCycle(0)
#         SPD2.ChangeDutyCycle(0)
#         SPD3.ChangeDutyCycle(0)
#         SPD4.ChangeDutyCycle(0)
# # Main loop for motion control
# def mpu():
#     # while True:
#     # Read accelerometer data from MPU6050
#         accelerometer_data = sensor.get_accel_data()
#         x = accelerometer_data['x']
#         y = accelerometer_data['y']
#         z = accelerometer_data['z']

#         # Calculate pitch and roll angles
#         pitch = 180 * math.atan2(x, math.sqrt(y*y + z*z)) / math.pi
#         roll = 180 * math.atan2(y, math.sqrt(x*x + z*z)) / math.pi

#         print(pitch)
#         print(roll)
        
#         # Determine motor direction and speed based on pitch and roll angles
#         if pitch > 7:
#             set_motor_speed('forward', 100)
#         elif pitch < -7:
#             set_motor_speed('backward', 100)
#         elif roll > 14:
#             set_motor_speed('right', 100)
#         elif roll < -14:
#             set_motor_speed('left', 100)
#         else:
#             set_motor_speed('stop', 0)

#         # Delay for 0.1 seconds before repeating loop
#         #time.sleep(0.1)




# high cw low acw
def F(speed): #forward

    GPIO.output(DIR1, GPIO.LOW)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.LOW) 
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)
    
    


def B(speed): #backward
    GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.HIGH) 
    GPIO.output(DIR4, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)
    


def R(speed): #left
    GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.HIGH) 
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)
    

def L(speed): #right
    GPIO.output(DIR1, GPIO.LOW)    # S
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.LOW) 
    GPIO.output(DIR4, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)
    	


def STOP():
    GPIO.output(DIR1, GPIO.HIGH)    # AC
    GPIO.output(DIR2, GPIO.HIGH)    # AC
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
   
        

def THROW(speed):
      GPIO.output(URD, GPIO.LOW)    # AC
      GPIO.output(LRD, GPIO.HIGH)    # C
      SPD_UR.ChangeDutyCycle(speed)
      SPD_LR.ChangeDutyCycle(speed)
      print(speed)

MSPEED = 0
PWM = 255
MAXSPEED = round((PWM/255) * 100)

PWMPTR = 0
startThrow = False
PWMCHNG = False
btn = None


# PWMSPD = [40, 40, 50, 50]
# # PWMPTRCNT = 3
# PWMPTR = 0

# PWMCHNG = False



#

# def deb():
#     print("here")
#     while True:
#         # F(100)
#         pygame.event.pump()
#         for event in pygame.event.get():
#             print(event)

# deb()


# Set initial motor direction and speed


           # x = round(joyStick.get_axis(2)*100)
           # y = round(joyStick.get_axis(3)*100)
           # spd = round(joyStick.get_axis(5)*100)/2 + 50
#while True           

while True:
    # mpu()
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            x = round(joyStick.get_axis(0)*100)      #left joystick   0,1,4
            y = -round(joyStick.get_axis(1)*100)                             
            spd = round(joyStick.get_axis(5)*100)/2 + 50
            z = joyStick.get_hat(0)
            # print(x)
            # print(y)
            print(spd)
            print(z)
            
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
            btn = event.button + 20\
        
        elif event.type == pygame.HAT_UP:
            btn=event.button

        if btn != None:
            if btn == 4: #L1 #throwstart
                startThrow = True
                PWMPTR = 0
        
            elif btn == 1: #O  #throwstop
                startThrow = False
                PWMPTR = 0
            
            elif btn == 5:  #pActuator
                print("SHACT")
                GPIO.output(SHACT, GPIO.LOW)

                #time.sleep(1)
                #GPIO.output(SHACT, GPIO.HIGH)

            elif btn == 25:
                GPIO.output(SHACT, GPIO.HIGH)

                
            elif btn == 3:  #pActuator pushing 
                print("SHACT")
                GPIO.output(SHACT, GPIO.LOW)

                #time.sleep(1)
                #GPIO.output(SHACT, GPIO.HIGH)

            elif btn == 23:
                GPIO.output(SHACT, GPIO.HIGH)


            

            
            elif btn == 2:#triangle claw down 
                GPIO.output(CLAW, GPIO.HIGH)
                SPD_CLAW.ChangeDutyCycle() 

            elif btn == 0: #cross Claw up
                GPIO.outout(CLAW, GPIO.LOW)
                SPD_CLAW.ChangeDutyCycle(spd)
            
            elif btn == 22 or btn == 20:
                GPIO.output(CLAW, GPIO.HIGH)
                #GPIO.output(CLAW, GPIO.LOW)
                SPD_CLAW.ChangeDutyCycle(0)
                

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