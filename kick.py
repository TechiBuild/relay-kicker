import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
relay_GPIO_PIN = 17
GPIO.setup(relay_GPIO_PIN, GPIO.OUT) # GPIO Assign mode

GPIO.output(relay_GPIO_PIN, GPIO.LOW) # out
GPIO.output(relay_GPIO_PIN, GPIO.HIGH) # on
