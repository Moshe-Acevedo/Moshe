from  nGPS01 import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.IN)
GPIO.setup(38,GPIO.IN)

while 1:
	x = Read(40,38)
	if x == 'ON':
		print "Success!"
		time.sleep(.2)
	else:
		pass
GPIO.cleanup()
