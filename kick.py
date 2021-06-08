import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
relay_1 = 17
relay_2 = 27

GPIO.setup(relay_1, GPIO.OUT) # GPIO Assign mode
GPIO.setup(relay_2, GPIO.OUT) # GPIO Assign mode

GPIO.output(relay_1, GPIO.LOW) # out
GPIO.output(relay_2, GPIO.LOW) # out
time.sleep(5)
GPIO.output(relay_1, GPIO.HIGH) # on
GPIO.output(relay_2, GPIO.HIGH) # on
time.sleep(5)
GPIO.output(relay_1, GPIO.LOW) # out
GPIO.output(relay_2, GPIO.LOW) # out
