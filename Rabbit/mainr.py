import RPi.GPIO as GPIO

pygame.init()
pygame.joystick.init()
try:
    joyStick =pygame.joystick.Joystick(0)
    joyStick.init()
except:
    pass
DIR1 = 22
DIR2 = 31
DIR3 = 33
DIR4 = 18
PWM_PIN_1 = 32
PWM_PIN_2 = 36
PWM_PIN_3 = 16    #38
PWM_PIN_4 = 12 #40

DIRB = 7       #claw
SPDB_PWM_PIN = 13   



SHACT = 15



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

GPIO.setup(DIRB, GPIO.OUT)
GPIO.setup(SPDB_PWM_PIN, GPIO.OUT)

SPD1 = GPIO.PWM(PWM_PIN_1, 1000)
SPD2 = GPIO.PWM(PWM_PIN_2, 1000)
SPD3 = GPIO.PWM(PWM_PIN_3, 1000)
SPD4 = GPIO.PWM(PWM_PIN_4, 1000)

SPDB = GPIO.PWM(SPDB_PWM_PIN, 1000)



SPD1.start(0)
SPD2.start(0)
SPD3.start(0)
SPD4.start(0)

SPDB.start(0)


# high cw low acw
def F(speed): #forward
    GPIO.output(DIR1, GPIO.LOW)    # S
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.LOW) 
    GPIO.output(DIR4, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)
    
def B(speed): #backward
    GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.HIGH) 
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)

def L(speed): #left
    GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.HIGH) 
    GPIO.output(DIR4, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)
    
def R(speed): #right
    GPIO.output(DIR1, GPIO.LOW)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.LOW) 
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(speed)
    
def FLD(speed): #forward left diagonal
	GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.LOW)    # C
    GPIO.output(DIR3, GPIO.HIGH) 
    GPIO.output(DIR4, GPIO.LOW)   # AC
    SPD1.ChangeDutyCycle(0)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(0)
    SPD4.ChangeDutyCycle(speed)
    
def FRD(speed): #forward right diagonal
	GPIO.output(DIR1, GPIO.LOW)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.LOW) 
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(speed)
    SPD2.ChangeDutyCycle(0)
    SPD3.ChangeDutyCycle(speed)
    SPD4.ChangeDutyCycle(0)

def BLD(speed): #backward left diagonal
	GPIO.output(DIR1, GPIO.HIGH)    # S
    GPIO.output(DIR2, GPIO.HIGH)    # C
    GPIO.output(DIR3, GPIO.HIGH) 
    GPIO.output(DIR4, GPIO.HIGH)   # AC
    SPD1.ChangeDutyCycle(0)
    SPD2.ChangeDutyCycle(speed)
    SPD3.ChangeDutyCycle(0)
    SPD4.ChangeDutyCycle(speed)

def FRD(speed): #backward right diagonal
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
        
    GPIO.output(DIRB, GPIO.HIGH)    
    SPD1.ChangeDutyCycle(0)
    SPD2.ChangeDutyCycle(0)
    SPD3.ChangeDutyCycle(0)
    SPD4.ChangeDutyCycle(0)
    SPDB.ChangeDutyCycle(0)

# MSPEED = 0
# PWM = 75
# MAXSPEED = round((PWM/255) * 100)
# PWMSPD = [40, 40, 50, 50]
# # PWMPTRCNT = 3
# PWMPTR = 0

# PWMCHNG = False


def set_motor_speed(direction,speed):

    if direction == 'forward':
        SPD1.ChangeDutyCycle(speed)
        SPD2.ChangeDutyCycle(speed)
        SPD3.ChangeDutyCycle(speed)
        SPD4.ChangeDutyCycle(speed)
    elif direction == 'backward':
        SPD1.ChangeDutyCycle(speed)
        SPD2.ChangeDutyCycle(speed)
        SPD3.ChangeDutyCycle(speed)
        SPD4.ChangeDutyCycle(speed)
    elif direction == 'left':
        SPD1.ChangeDutyCycle(speed)
        SPD2.ChangeDutyCycle(0)
        SPD3.ChangeDutyCycle(speed)
        SPD4.ChangeDutyCycle(0)
    elif direction == 'right':
        SPD1.ChangeDutyCycle(0)
        SPD2.ChangeDutyCycle(speed)
        SPD3.ChangeDutyCycle(0)
        SPD4.ChangeDutyCycle(speed)
    else:
        SPD1.ChangeDutyCycle(0)
        SPD2.ChangeDutyCycle(0)
        SPD3.ChangeDutyCycle(0)
        SPD4.ChangeDutyCycle(0)
# Main loop for motion control
def mpu():
    # while True:
    # Read accelerometer data from MPU6050
        accelerometer_data = sensor.get_accel_data()
        x = accelerometer_data['x']
        y = accelerometer_data['y']
        z = accelerometer_data['z']

        # Calculate pitch and roll angles
        pitch = 180 * math.atan2(x, math.sqrt(y*y + z*z)) / math.pi
        roll = 180 * math.atan2(y, math.sqrt(x*x + z*z)) / math.pi

        # Determine motor direction and speed based on pitch and roll angles
        if pitch > 5:
            set_motor_speed('forward', 50)
        elif pitch < -5:
            set_motor_speed('backward', 50)
        elif roll > 5:
            set_motor_speed('right', 50)
        elif roll < -5:
            set_motor_speed('left', 50)
        else:
            set_motor_speed('stop', 0)

        # Delay for 0.1 seconds before repeating loop
        #time.sleep(0.1)

