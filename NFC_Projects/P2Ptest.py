import nxppy
import time
mifare = nxppy.Mifare()

while 1:	
	try:
		time.sleep(1)
		uid = mifare.select()
		print(uid)
	except nxppy.SelectError:
		pass
	
