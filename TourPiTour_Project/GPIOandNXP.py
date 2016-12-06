import nxppy
import RPi.GPIO as GPIO
import time
mifare = nxppy.Mifare()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.output(40,True)
while 1:
	time.sleep(3)
	GPIO.output(40,True)
	try:
		uid = mifare.select()
		GPIO.output(40,False)
		print uid
		pass
	except nxppy.SelectError:
		pass

