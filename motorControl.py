import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO

import time

def stop():
	print 'stop'
	PWM.start("P8_46",0)
        PWM.start("P8_36",0)
        PWM.start("P8_45",0)
        PWM.start("P8_34",0)
	time.sleep(1)
	return 

def forward():
	PWM.start("P8_46", 100)
	PWM.start("P8_36", 100)
	return	

def backward():
        PWM.start("P8_34", 100)
        PWM.start("P8_45", 100)
	print 'backward'
        return

def left():
        PWM.start("P8_46", 100)
	print 'left'
        return
        
def right():
        PWM.start("P8_45", 100)
	print 'right'
        return

def leftb():
        PWM.start("P8_34", 100)
        PWM.start("P8_46", 100)
	print 'leftb'
	return

def rightb():
        PWM.start("P8_45", 100)
        PWM.start("P8_36", 100)
	print 'rightb'
	return

def leftb_delay(delay):
	print 'left_d'
        PWM.start("P8_34", 100)
        PWM.start("P8_46", 100)
	time.sleep(delay)
	stop()        
        return 
    
def rightb_delay(delay):
	print 'rightb_d'
        PWM.start("P8_45", 100)
        PWM.start("P8_36", 100)	
	time.sleep(delay)
	stop()
        return

def right_delay(delay):
	print 'right_delay'
	right()
	time.sleep(delay)
	return

def left_delay(delay):
	print 'left_delay'
	left()
	time.sleep(delay)
	return



