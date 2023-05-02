import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
x = 8
BUTTON_PIN = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(x, GPIO.OUT, initial=GPIO.HIGH)
while True:
    GPIO.output(x, GPIO.HIGH)
    sleep(1)
    GPIO.wait_for_edge(BUTTON_PIN, GPIO.RISING)
    print("Button Pressed")
    GPIO.output(x, GPIO.LOW)
    sleep(1)
    GPIO.wait_for_edge(BUTTON_PIN, GPIO.RISING)
    print("Button Pressed")
    GPIO.output(x, GPIO.HIGH)
    sleep(1)
GPIO.cleanup()
