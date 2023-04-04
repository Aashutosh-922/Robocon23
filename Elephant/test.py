
import RPi.GPIO as GPIO
import time

DIR1 = 7
DIR2 = 12
DIR3 = 16
DIR4 = 18
PWM_PIN_1 = 22
PWM_PIN_2 = 36
PWM_PIN_3 = 38
PWM_PIN_4 = 40
DIRB = 11
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

#def main(): #high
print("high")
while(1):
	
	GPIO.output(DIR1, GPIO.HIGH)    # S
	GPIO.output(DIR2, GPIO.HIGH)    # C
	GPIO.output(DIR3, GPIO.HIGH) 
	GPIO.output(DIR4, GPIO.HIGH)   # AC
	
	GPIO.output(PWM_PIN_1, GPIO.HIGH)    # S
	GPIO.output(PWM_PIN_2, GPIO.HIGH)    # C
	GPIO.output(PWM_PIN_3, GPIO.HIGH) 
	GPIO.output(PWM_PIN_4, GPIO.HIGH)   # AC
		
	GPIO.output(SHACT, GPIO.HIGH)
	GPIO.output(DIRB, GPIO.HIGH)
	GPIO.output(SPDB_PWM_PIN, GPIO.HIGH)
		
		

