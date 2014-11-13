import Adafruit_BBIO.ADC as ADC #Similar to analog read
import time as T
import math as m

def IRread():
	# Useful Lists:
	IR1list = []
	IR2list = []
	IR3list = []
	IR4list = []
	IR5list = []

	# General purpose variables:
	count = 0
	samples = 20
	voltMulti = 6.3

	ADC.setup()

	# Reading analog inputs:
	IR1 = ADC.read("P9_40") * voltMulti #added a voltage multiplier
	IR2 = ADC.read("P9_39") * voltMulti
	IR3 = ADC.read("P9_38") * voltMulti
	IR4 = ADC.read("P9_37") * voltMulti
	IR5 = ADC.read("P9_35") * voltMulti

	for i in range(samples):
		count = count + 1

		IR1list.append(IR1)
		IR2list.append(IR2)
		IR3list.append(IR3)
		IR4list.append(IR4)
		IR5list.append(IR5)

		if (count == samples):
			# Calculating the average of 20 readings:
			avgIR1 = round(sum(IR1list) / len(IR1list),2)
			avgIR2 = round(sum(IR2list) / len(IR2list),2)
			avgIR3 = round(sum(IR3list) / len(IR3list),2)
			avgIR4 = round(sum(IR4list) / len(IR4list),2)
			avgIR5 = round(sum(IR5list) / len(IR5list),2)
			
			# Clearing each list:
			IR1list = []
			IR2list = []
			IR3list = []
			IR4list = []
			IR5list = []
			count = 0

	return (avgIR1, avgIR2, avgIR3, avgIR4, avgIR5)

def distanceCalc(volt):
	# NOTE: This function works only if you position the sensor 10cm from the edge.
	return (41.543 * m.pow((volt + 0.30221), -1.5281))

	
''' Main code: '''

while True:

	r1A, r1B, r1C, r1D, r1E = IRread()

	measA = distanceCalc(r1A)
	measB = distanceCalc(r1B)
	measC = distanceCalc(r1C)
	measD = distanceCalc(r1D)
	measE = distanceCalc(r1E)

	print '\nReading A: ' + str(measA)
	print '\nReading B: ' + str(measB)
	print '\nReading C: ' + str(measC)
	print '\nReading D: ' + str(measD)
	print '\nReading E: ' + str(measE)
	
	T.sleep(0.5)
