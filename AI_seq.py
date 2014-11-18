import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import random as rand
from IRread import IRread, distanceCalc


# Global Variables:
ninty = .4
slight = .1

# IR sensor threasholds (in cm):
frontLow = 35
rightLow = 25
leftLow  = 25


farfromright = 45
farfromleft = 45
frontHigh = frontLow + 10
rightHigh = rightLow + 10
leftHigh  = leftLow + 10

sideWall = 0

low_PWM = 78
high_PWM = 80

''' Main Code: '''
PWM.start("P8_46",0)
PWM.start("P8_45",0)
PWM.start("P8_36",0)
PWM.start("P8_34",0)

time.sleep(10)

while True:
	time.sleep(0.25) #VITAL!!

        # Reads each of the IR sensors:
        front, NLeft, left, right, Nright = IRread()

       

        # Calculates their values in cm:
        cmFront = distanceCalc(front)
        #cmFleft = distanceCalc(fLeft) # Use this only for turns
        #cmFright = distanceCalc(fRight) # Use this only for turns
        cmRight = distanceCalc(right)
        cmLeft = distanceCalc(left)

	if sideWall == 0:
		print 'sw 0'
		if cmFront > frontLow:
			PWM.start("P8_36",high_PWM)
			PWM.start("P8_46",high_PWM)
		else:
			PWM.start("P8_46",0)
			PWM.start("P8_45",0)
			PWM.start("P8_36",0)
			PWM.start("P8_34",0)
			time.sleep(1)

			if cmRight < cmLeft:
				sideWall = 2
				print 'Left'
				PWM.start("P8_36",0)
                                PWM.start("P8_45",0)
				PWM.start("P8_34",high_PWM)
	                        PWM.start("P8_46",high_PWM)
				time.sleep(ninty)
				PWM.start("P8_34",0)
                                PWM.start("P8_46",0)
				time.sleep(1)
		


			else:
				sideWall = 1
				print 'Right'
                                PWM.start("P8_34",0)
                                PWM.start("P8_46",0)
		                PWM.start("P8_36",high_PWM)
                                PWM.start("P8_45",high_PWM)
                                time.sleep(ninty)
                                PWM.start("P8_36",0)
                                PWM.start("P8_45",0)
				time.sleep(1)
		
	elif sideWall == 2:
		print 'sw 2'
		if cmFront > frontLow:
			if cmRight > rightLow and cmRight < rightHigh:
				print 'forward'
				PWM.start("P8_36",high_PWM)
                       		PWM.start("P8_46",high_PWM)
			elif cmRight < rightLow:
				print 'Slight Left'
				PWM.start("P8_36",high_PWM)
                        	PWM.start("P8_46",low_PWM)
			elif cmRight >= farfromright:
                        	sideWall = 0
                        	PWM.start("P8_46",0)
                        	PWM.start("P8_45",0)
                        	PWM.start("P8_36",0)
                        	PWM.start("P8_34",0)
			elif cmRight > rightHigh:
				print 'Slight Right'
				PWM.start("P8_36",low_PWM)
                        	PWM.start("P8_46",high_PWM)
		else:
			print 'turning'
                        PWM.start("P8_36",0)
                        PWM.start("P8_45",0)
                        PWM.start("P8_34",high_PWM)
                        PWM.start("P8_46",high_PWM)
                        time.sleep(ninty)
                        PWM.start("P8_34",0)
                        PWM.start("P8_46",0)



	
	elif sideWall == 1:
		print 'sw 1'
		if cmFront > frontLow:
			if cmLeft > leftLow and cmLeft < leftHigh:
				print 'forward'
	                        PWM.start("P8_36",high_PWM)
	                        PWM.start("P8_46",high_PWM)
			elif cmLeft < leftLow:
				print 'Right'
				PWM.start("P8_36",low_PWM)
                        	PWM.start("P8_46",high_PWM)
                	elif cmLeft >= farfromleft:
                        	sideWall = 0
                        	PWM.start("P8_46",0)
                        	PWM.start("P8_45",0)
                        	PWM.start("P8_36",0)
                        	PWM.start("P8_34",0)
			elif cmLeft > leftHigh:
				print 'left'
				PWM.start("P8_36",100)
                        	PWM.start("P8_46",low_PWM)
		else:
			PWM.start("P8_34",0)
                        PWM.start("P8_46",0)
                        PWM.start("P8_36",high_PWM)
                        PWM.start("P8_45",high_PWM)
                        time.sleep(ninty)
                        PWM.start("P8_36",0)
                        PWM.start("P8_45",0)



	else:
		stop()
	
	
