import Adafruit_BBIO.GPIO as GPIO


GPIO.setup("P9_11", GPIO.IN) #OUTA
GPIO.setup("P9_12", GPIO.IN) #OUTB

GPIO.add_event_detect("P9_11", GPIO.RISING)
GPIO.add_event_detect("P9_12", GPIO.RISING)

while True:

	if GPIO.event_detected("P9_11") or GPIO.event_detected("P9_12"):
		print 'Robot is moving.\n'

