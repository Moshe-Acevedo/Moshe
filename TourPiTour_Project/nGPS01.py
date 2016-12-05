import RPi.GPIO as GPIO
import time

def Read(c,d):
	e=[]
	if GPIO.input(c) == True:
		e.append('1')
	else:
		e.append('0')
	if GPIO.input(d) == True:
		e.append('1')
	else:
		e.append('0')
	f = ''.join(e)
	if f == '11':
		z = 'ON'
	else:
		z = 'OFF'
	return z

def Write(g,h,i):
	if g == 'ON':
		GPIO.output(h, True)
		GPIO.output(i, True)
	if g == 'OFF':
		GPIO.output(h, False)
		GPIO.output(i, False)
