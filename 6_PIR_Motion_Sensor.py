import RPi.GPIO as GPIO
PIR_Input = 29
LED = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_Input, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
while True:
    if GPIO.input(PIR_Input):
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
# V GPIO G

# Alternative
from gpiozero import MotionSensor
from Rpi import GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED=12

GPIO.setup(LED, GPIO.OUT)
sensor = MotionSensor(14)

while True:
    GPIO.output(LED, GPIO.LOW)
    sensor.wait_for_motion()
    GPIO.output(LED, GPIO.HIGH)
    print("Moved")
    sensor.wait_for_no_motion()
