import RPi.GPIO as GPIO
from gpiozero import Buzzer
import time
try:
    GPIO.setmode(GPIO.BOARD)
    BUZZER_PIN = 18
    buzzer = Buzzer(BUZZER_PIN)
    PIN_TRIGGER = 7
    PIN_ECHO = 11
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print("Distance:", distance, "cm")
    time.sleep(0.001)
    if distance < 10:
        counter = 10000
        while counter > 0:
            buzzer.on()
            time.sleep(0.0001)
            buzzer.off()
            time.sleep(0.0001)
            counter = counter - 1
finally:
    GPIO.cleanup()
# VCC Trig Echo GND
