import Adafruit_BBIO.PWM as PWM
import time

# Moving Left Wheel forward CCW:
PWM.start("P8_46", 100)
time.sleep(5)
PWM.stop("P8_46")

time.sleep(2)

# Moving Left Wheel backward CW:
PWM.start("P8_45", 100)
time.sleep(5)
PWM.stop("P8_45")

time.sleep(2)

# Moving Right Wheel forward CCW:
PWM.start("P8_36", 100)
time.sleep(5)
PWM.stop("P8_36")

time.sleep(2)

# Moving Right Wheel backward CW:
PWM.start("P8_34", 100)
time.sleep(5)
PWM.stop("P8_34")

time.sleep(2)

# Moving forward:
PWM.start("P8_46", 100)
PWM.start("P8_36", 100)
time.sleep(5)
PWM.stop("P8_46")
PWM.stop("P8_36")

time.sleep(2)

# Reverse:
PWM.start("P8_45", 100)
PWM.start("P8_34", 100)
time.sleep(5)
PWM.stop("P8_45")
PWM.stop("P8_34")

time.sleep(2)

# Turning Right:
PWM.start("P8_46", 50)
PWM.start("P8_34", 50)
time.sleep(1)
PWM.stop("P8_34")
PWM.stop("P8_46")

time.sleep(2)

# Turning Left
PWM.start("P8_36", 50)
PWM.start("P8_45", 50)
time.sleep(1)
PWM.stop("P8_45")
PWM.stop("P8_36")

PWM.cleanup()

