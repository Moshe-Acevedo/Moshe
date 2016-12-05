from gopigo import *
import time
from math import *
import nGPS01
import RPi.GPIO as GPIO

######################################################################################
# 
# _To_do_ List_
# Check servo functions for ScanWall().
# Finish CheckForCard().
# Try to write PosProject(), check gopigo.py for wheel distance calculations.
# Test without CheckForCard().
# Test in Conjunction with All Systems. 
#
######################################################################################

def StartUp():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(40,GPIO.IN)
	GPIO.setup(38,GPIO.IN)
	GPIO.setup(36,GPIO.IN)
	GPIO.setup(32,GPIO.OUT)
	enable_servo()
	print "TourPiTour v0.7.2"
	time.sleep(3)

def GetDistance():
	d = us_dist(analogPort)
	return d
	
def ScanWall():
	servo(90)
	for x in xrange(19):
		servo(90-(5*x))
		time.sleep(0.05)
	r = GetDistance()
	for x in xrange(38):
		time.sleep(.05)
		servo(x*5)
	l = GetDistance()
	if r < l:
		dir = 'Right'
		for x in xrange(19):
			servo(180-(10*x))
			time.sleep(.05)
	else:
		dir = 'Left'
	return dir		

def CalculateTurn(Direction):
	time.sleep(.2)
	c = GetDistance()
	time.sleep(.1)
	servo(103)
	time.sleep(.1)
	b = GetDistance()
	time.sleep(.1)
	chicken = pow(b,2) + pow(c,2) - 2*b*c*cos(pi/6)
	a = sqrt(chicken)
	chicken2 = (float(c)*sin(pi/6))/a
	chicken3 = asin(chicken2)
	chicken4 = chicken3*180.0/pi
	return chicken4, c
	

	
def FirstFix(dir):
	servo(73)
	time.sleep(.2)
	a , c = CalculateTurn(dir)
	fwd(c)
	WaitToStop()
	if dir == 'Left':
		turn_right(a)
	if dir == 'Right':
		turn_left(a)
	time.sleep(.5)

def CheckForCard():
	if  Read(40,38) == 'ON':
		return 'Chicken'

def PosProject(dir):
	stop()
	time.sleep(1)
	if dir == 'Left':
		turn_right(90)
		while 1:
			time.sleep(.1)
			if Read(40,38) == 'ON':
				break	
		turn_left(90)
	if dir == 'Right':
		turn_left(90)
		while 1:
			time.sleep(.1)
			if Read(40,38) == 'ON':
				break
		turn_right()
	fwd()
	
def WaitToStop():
	while 1:
		distance1 = GetDistance()
		time.sleep(.5)
		distance2 = GetDistance()
		if distance1 == distance2:
			break

def FollowWall(dir,x):
	fwd()
	set_speed(200)
	while 1:
		if Read(40,38) == 'ON':
			PosProject(dir)
		else:
			pass
		Distance1 = GetDistance()
		time.sleep(.1)
		Distance2 = GetDistance()
		z = Distance1-Distance2  ## check this 
		if z > 0:
			zed = z//0.5
			set_left_speed(spd-1-zed)
		else:
			set_left_speed(spd)
		if z < 0:
			z = 0 - z
			zed = z // 0.5
			set_right_speed(spd-1-zed)
		else:
			set_right_speed(spd)
		if GPIO.input(36):
			break
		else:
			pass
		x=x+1
		if x == 400:
			break
		
def CleanUp():
	stop()
	disable_servo()

time.sleep(5)
#StartUp()
Direction = 'Left'
print Direction
servo(72)
time.sleep(0.5)
a,c = CalculateTurn('Left')
print a, c
x = 0
#FollowWall(Direction,x)
#CleanUp()
