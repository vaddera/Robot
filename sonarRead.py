import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_15", GPIO.OUT) # Trigger
GPIO.setup("P9_23", GPIO.IN) # Echo

GPIO.output("P9_15", GPIO.LOW)

time.sleep(2) # setup time delay

while True:

	time.sleep(0.5)

	GPIO.output("P9_15", GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output("P9_15", GPIO.LOW)
	
	while GPIO.input("P9_23") == False:
		signaloff = time.time()

	while GPIO.input("P9_23") == True:
		signalon = time.time()

	t = signalon - signaloff
	d = t*17000
	print d
