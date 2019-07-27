import PiMotor
import time
import RPi.GPIO as gpio
import random


m1 = PiMotor.Motor("MOTOR1", 1)
m2 = PiMotor.Motor("MOTOR2", 1)
m3 = PiMotor.Motor("MOTOR3", 1)
m4 = PiMotor.Motor("MOTOR4", 1)

motorAll = PiMotor.LinkedMotors(m1, m2, m3, m4)

motorLeft = PiMotor.LinkedMotors(m1, m2)
motorRight = PiMotor.LinkedMotors(m3, m4)

sensor = PiMotor.Sensor("ULTRASONIC", 30)

sensor.trigger()

print sensor.Triggered

arrowForward = PiMotor.Arrow(3)
arrowReverse = PiMotor.Arrow(4)
arrowBack = PiMotor.Arrow(1)
arrowLeft = PiMotor.Arrow(2)

def checkDirection():
	possibleDirections = []

	motorAll.stop()
	time.sleep(0.1)

	motorLeft.forward(100)
	motorRight.reverse(100)
	time.sleep(0.8)
	motorLeft.stop()
	motorRight.stop()

	sensor.trigger()
	time.sleep(0.5)
	if (sensor.Triggered == False):
		possibleDirections.append("RIGHT")

	motorLeft.reverse(100)
	motorRight.forward(100)
	time.sleep(1.4)
	motorLeft.stop()
	motorRight.stop()

	sensor.trigger()
	time.sleep(0.5)
	if (sensor.Triggered == False):
		possibleDirections.append("LEFT")

	possibleDirections.append("BACKWARDS")

	return possibleDirections

def forward():
	while sensor.Triggered == False:
		arrowForward.on()
		motorAll.forward(100)
		sensor.trigger()


while True:

	forward()

	possibleDirections = checkDirection()

# pick a direction, could be backward, right or left

	chosenDirection = possibleDirections[random.randrange(len(possibleDirections))]

	print chosenDirection

	if (chosenDirection == "LEFT"):
		# do left, go forward
		time.sleep(0.1)
	elif (chosenDirection == "RIGHT"):
		# do right stuff, turn 180 and go forward
		motorLeft.forward(100)
		motorRight.reverse(100)
		time.sleep(1.4)
		motorLeft.stop()
		motorRight.stop()
	else:
		# do backwards, turn 90 degrees right, go backwards, change direction, go forwards
		motorLeft.forward(100)
		motorRight.reverse(100)
		time.sleep(0.6)
		motorAll.reverse(100)
		time.sleep(1)
		motorAll.stop()
		time.sleep(0.3)
		motorLeft.forward(100)
		motorRight.reverse(100)
		time.sleep(random.randrange(1, 4))

