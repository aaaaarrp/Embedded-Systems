# In Order
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
n = [3, 7, 11]
for i in n:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
while True:
    for i in n:
        GPIO.output(i, GPIO.HIGH)
        sleep(1)
        GPIO.output(i, GPIO.LOW)

# Reverse Order
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
n = [11, 7, 3]
for i in n:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
while True:
    for i in n:
        GPIO.output(i, GPIO.HIGH)
        sleep(1)
        GPIO.output(i, GPIO.LOW)

# Random Order
import RPi.GPIO as GPIO
from time import sleep
import random
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
n = [3, 7, 11]
for i in n:
    GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
while True:
    i = random.randint(0, 2)
    GPIO.output(n[i], GPIO.HIGH)
    sleep(1)
    GPIO.output(n[i], GPIO.LOW)
