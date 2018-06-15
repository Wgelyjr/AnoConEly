#A module for monitoring script execution time
#Begin the script with var = timekeep.start(), finish with timekeep.finish(var)
import time
def start():
	x = time.time()
	return(x)
	
def finish(timestart):
	tottime = time.time() - timestart
	minu = " minutes."
	hou = " hours."
	seco = " seconds."
	tottime = (round((float(time.time()) - float(timestart)), 3))
	totmin = tottime/60
	tothr = totmin/60

	if tottime > 3600:
		x = round(tothr,3)
		y = hou
	elif tottime > 90:
		x = round(totmin,3)
		y = minu
	else:
		x = round(tottime,3)
		y = seco
	z = "Executed in " + str(x) + y
	print(z)