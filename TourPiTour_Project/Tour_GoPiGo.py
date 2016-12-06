import nxppy
import time
import subprocess
import RPi.GPIO as GPIO
from nGPS01 import *

print "TourPiTour v0.5.3 starting up..."

mifare = nxppy.Mifare()
GPIO.setwarnings(False)
list = []
uid = 'chicken'
uidb = 'chicken'
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(32,GPIO.IN)

def CheckCard(uid):
	uidx = uid
	try:
		uidx = mifare.select()
		time.sleep(.2)
	except nxppy.SelectError:
		pass
	if uidx != uid:
		return True
	else:
		return False
	print "I checked yo"

time.sleep(5)
while 1:
	try:
		uid = mifare.select()
	except nxppy.SelectError:
		pass
	if uid != uidb:
		uidb = uid
		uidb = str(uidb)
		if uid == '04A3E5D26F3F80':
			print 'VTC'
			Write('ON',40,38)
			time.sleep(.1)
			Write('OFF',40,38)
			subprocess.call("./VideoPlayerBash.sh &", shell = True)
			while 1:
				time.sleep(.5)
				proc = subprocess.Popen('ps -al | grep omxplayer', stdout = subprocess.PIPE, shell = True)
				time.sleep(.1)
				tmp = proc.stdout.read()
				print "I checked"
				try:
					if tmp[0] != '0':
						print "I Broke"
						break
				except:		
					break
				if CheckCard(uidb):
					break	
			subprocess.call("./VideoKiller.sh", shell = True)
