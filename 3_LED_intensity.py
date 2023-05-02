# Pattern 1
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
P = GPIO.PWM(3, 100)
GPIO.setup(7, GPIO.OUT)
Q = GPIO.PWM(7, 100)
GPIO.setup(11, GPIO.OUT)
R = GPIO.PWM(11, 100)
GPIO.setup(15, GPIO.OUT)
S = GPIO.PWM(15, 100)

P = start(0)
Q = start(0)
R = start(0)
S = start(0)

while True:
    for x in range(10, 100, 10):
        P.changeDutyCycle(x)
        Q.changeDutyCycle(x-2)
        R.changeDutyCycle(x-4)
        S.changeDutyCycle(x-6)
    for x in range(100, 10, -10):
        P.changeDutyCycle(x)
        Q.changeDutyCycle(x-2)
        R.changeDutyCycle(x-4)
        S.changeDutyCycle(x-6)
    sleep(0.1)
