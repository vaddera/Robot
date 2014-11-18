
About the Project:

The objective of this project is to create an autonomous Robot based on Beaglebone Black. The robot's structure is consisted basically of two parallel back tractioned wheels, a guideball on the front, 3 Infrared rangefinders and two digital rotation encoders.

The first type of sensor that is able to interact with the BBB is the Magician Robot encoder from Sparkfun which is successfully working and being read by a python script.

The second type of sensor that can be read is the IR distance sensor and they can be a little tricky to deal due to their non-linear nature, but putting them 10 centimeters away from the edge and using an equation to correlate the voltage to a distance works.

In the end we want an autonomous robot that can find and hug walls using the IR sensors, and then use the rotary encoders to detect when the robot is in a stalled state. Along side this we made hardware in the form of a cape to hold all the components needed.

To the right you can see the completed robot hardware.

-----------------------------------------------------------------------------------------------

Installation Instructions:

This project was developed in python which has a simple API created by Adafruit called Beaglebone Black IO - BBIO.

To install Adafruit's BBIO follow the instructions below. These installation instructions are for Debian and Ubuntu distributions:

1 - Update your Operating System and install the dependencies:

bone$ sudo apt-get update
bone$ sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus -y
2 - Next install the BBIO:

bone$ sudo pip install Adafruit_BBIO
3 - Verify if the BBIO was installed properly:

bone$ sudo python -c "import Adafruit_BBIO.GPIO as GPIO; print GPIO"
# You should see the following message:
bone$ <module 'Adafruit_BBIO.GPIO' from '/usr/local/lib/python2.7/dist-packages/Adafruit_BBIO/GPIO.so'>
If the previous installation method fails, install it manually:

1 - Update and install the depencencies:

bone$ sudo apt-get update
bone$ sudo apt-get install build-essential python-dev python-pip python-smbus -y
2 - Clone the BBIO's git repository and change into the directory it was downloaded into:

bone$ git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
bone$ cd adafruit-beaglebone-io-python
3 - Install the API and remove the installation file:

bone$ sudo python setup.py install
bone$ cd ..
bone$ sudo rm -rf adafruit-beaglebone-io-python
The specifics on how to use this API in Python can be found on the following link provided by Adafruit.

The python scripts used on the project can be found in this git repository.


Be sure your README.md is includes an up-to-date and clear description of your project so that someone who comes across you git repository can quickly learn what you did and how they can reproduce it.
If there is extra hardware needed, include links to where it can be obtained.

-----------------------------------------------------------------------------------------------

User Instructions:

Programming Tools and Instructions

Our group used python as the base for our program and you can do multiple tings with the code base that is in Github

motorControl.py

   -In our motor control code we setup functions that the user can use to properly set the PWM to make the robots move in specific directions. The following is included in the file
   stop()
       -This command stops all PWM pins thus stopping the robot.
   forward()
       - This command starts moving the robot forward. It does not stop the robot.
   backward()
       - This command starts moving the robot backward. It does not stop the robot.
   left()
       - This command starts turning  the robot left using one motor.
   right()
       - This command starts turning the robot right using one motor.
   leftb()
       - This command starts turning the robot left using both motors.
   rightb()
       - This command starts turnning the robot right using both motors.
   right_delay(delay)
       - This command turns the robot right for a specific amount of time, delay, using only one motor.
   left_delay(delay)
       - This command turns the robot left for a specific amount of time, delay, using only one motor.
   rightb_delay(delay)
       - This command turns the robot right for a specific amount of time, delay, using both motors.
   leftb_delay(delay)
       - This command turns the robot left for a specific amount of time, delay, using both motors.
run

   - This small program is used to test out the motor control functions and to conferm the motor pins are connected correctly.
IRread.py

   - This program reads the sensor values for the IR sensors off the analog pins and returns thier value, and also calculates distance from that value. This file contains two useful functions
   Out1, Out2, Out3, Out4, Out5, Out6 = IRread()
   distance = distanceCalc(out)
read

   - This small program prints out the read values from the IR sensors. This is useful for finding the correct voltage multiplier and judge distances with the sensor. Essentially seeing what the robot is seeing
AI_seq.py

This file contains our basic AI. This program finds a wall and then hugs it. If it unhuggs a wall if it gets to far, the robot finds another wall.

       The following options change the settings in terms of follwing a wall
       frontLow - This is the lower bond on distance you want your front sensor to read. The higher the number, the larger the buffer you give the robot.
       rightLow - This is the lower bond on distance you want your right sensor to read. The higher the number, the larger the buffer you give the robot.
       leftLow  - This is the lower bond on distance you want your left sensor to read. The higher the number, the larger the buffer you give the robot.
       rightHigh - When following a wall. This is the max distance you want the robot to get away from the wall when the wall is on the right side of the robot.
       leftHigh - When following a wall. This is the max distance you want the robot to get away from the wall when the wall is on the left side of the robot.
       farfromright - This is the distance you want your robot to give up and start finding another wall on the right side
       farfromleft  - This is the distance you want your robot to give up and start finding another wall on the right side
       The following two commands deal with the motor control of the robot. The farther apart they are the faster it turns away/toward a wall. The higher the number, the faster the overall operation is.
       low_PWM  - When turning away from the wall the robot slows a motor down to this low_PWM to have a slight turn.
       high_PWM - This is the max level the motors run at.
       The following variable controls the turn delay to make a 90 degree turn
       ninty - Sets delay when turning to create a full 90 degree turn
How to Run on the Robot

We used a portable USB pack and constructed a cable to attach it to the barrel connector. This allows you to program the robot, unplug the USB, and the watch it run on the floor/test area.

   Steps
   1. Attach both USB and barrel connector from protable battery pack
   2. ssh into your bone
   3. Add a delay to the start of you program using the time library (time.sleep(delay)
   4. Run the python program using the 'python' command
   5. Unplug the USB and set your robot on the flooor