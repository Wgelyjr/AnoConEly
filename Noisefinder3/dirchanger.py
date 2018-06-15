import os
import sys
#Organizes output files into folders.
def swap():
	olddir = os.path.dirname(os.path.realpath(sys.argv[1]))
	dirlist = os.listdir()
	csvlist = []
	pnglist = []
	for file in dirlist:
		if file.endswith(".csv"):
			csvlist.append(file)
		elif file.endswith(".png"):
			pnglist.append(file)
	try:
		os.makedirs(olddir + r"\\NoiseTables\\")
	except OSError:
		pass
	try:
		os.makedirs(olddir + r"\\CountPlots\\")
	except OSError:
		pass
	for file in csvlist:
		try:
			os.rename((olddir + "\\" + file),(olddir + r"\\NoiseTables\\" + file))
		except OSError:
			print("Clear out NoiseTables/CountPlots folders prior to running this script.")
			quit()
	for file in pnglist:
		try:
			os.rename((olddir + "\\" + file),(olddir + r"\\CountPlots\\" + file))
		except:
			print("Clear out NoiseTables/CountPlots folders prior to running this script.")
			break