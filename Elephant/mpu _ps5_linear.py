# Import necessary libraries
import RPi.GPIO as GPIO
import time
from mpu6050 import mpu6050

# Initialize MPU6050
mpu = mpu6050(0x68)

# Set GPIO pins for motor control
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Set PWM pins for motor control
motor1 = GPIO.PWM(11, 50)
motor2 = GPIO.PWM(12, 50)
motor3 = GPIO.PWM(13, 50)
motor4 = GPIO.PWM(15, 50)

# Set initial motor speed and duty cycle
motor1.start(0)
motor2.start(0)
motor3.start(0)
motor4.start(0)

# Set initial motor direction and speed
def set_motor_speed(direction, speed):
    if direction == 'forward':
        motor1.ChangeDutyCycle(speed)
        motor2.ChangeDutyCycle(speed)
        motor3.ChangeDutyCycle(speed)
        motor4.ChangeDutyCycle(speed)
    elif direction == 'backward':
        motor1.ChangeDutyCycle(speed)
        motor2.ChangeDutyCycle(speed)
        motor3.ChangeDutyCycle(speed)
        motor4.ChangeDutyCycle(speed)
    elif direction == 'left':
        motor1.ChangeDutyCycle(speed)
        motor2.ChangeDutyCycle(0)
        motor3.ChangeDutyCycle(speed)
        motor4.ChangeDutyCycle(0)
    elif direction == 'right':
        motor1.ChangeDutyCycle(0)
        motor2.ChangeDutyCycle(speed)
        motor3.ChangeDutyCycle(0)
        motor4.ChangeDutyCycle(speed)
    else:
        motor1.ChangeDutyCycle(0)
        motor2.ChangeDutyCycle(0)
        motor3.ChangeDutyCycle(0)
        motor4.ChangeDutyCycle(0)

# Main loop for motion control
while True:
    # Read accelerometer data from MPU6050
    accelerometer_data = mpu.get_accel_data()
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
    time.sleep(0.5)
