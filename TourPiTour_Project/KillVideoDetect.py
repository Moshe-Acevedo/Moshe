import subprocess 
import time

subprocess.call("./VideoPlayerBash.sh &", shell = True)
while 1:
	time.sleep(2)
	proc = subprocess.Popen('ps -al | grep omxplayer', stdout = subprocess.PIPE, shell = True)
	tmp = proc.stdout.read()
	if tmp[0] != '0':
		break
	else:
		pass
print "It broke"
