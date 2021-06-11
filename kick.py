import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD) # GPIO Numbers instead of board numbers

relay_1 = 32
relay_2 = 36

GPIO.setup(relay_1, GPIO.OUT) # GPIO Assign mode
GPIO.setup(relay_2, GPIO.OUT) # GPIO Assign mode

while True:

  # Button Off
  GPIO.output(relay_1, GPIO.HIGH)
  GPIO.output(relay_2, GPIO.HIGH)
  time.sleep(10)
  # Button On
  GPIO.output(relay_1, GPIO.LOW)
  GPIO.output(relay_2, GPIO.LOW)
  time.sleep(1)
