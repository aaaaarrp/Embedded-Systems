import RPi.GPIO as GPIO
from time import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

# g f a b c d e
digit0 = [0,1,1,1,1,1,1]
digit1 = [0,0,0,1,1,0,0]
digit2 = [1,0,1,1,0,1,1]
digit3 = [1,0,1,1,1,1,0]
digit4 = [1,1,0,1,1,0,0]
digit5 = [1,1,1,0,1,1,0]
digit6 = [1,1,1,0,1,1,1]
digit7 = [0,0,1,1,1,0,0]
digit8 = [1,1,1,1,1,1,1]
digit9 = [1,1,1,1,1,1,0]
arr = [digit0, digit1, digit2, digit3, digit4, digit5, digit6, digit7, digit8, digit9]
gpin = [3, 5, 8, 11, 13, 15, 19]

while True:
    for digit in arr:
        for i in range(0, 7):
            GPIO.output(gpin[i], digit[i])
        time.sleep(1)
# g f G a b
# e d G c dp

