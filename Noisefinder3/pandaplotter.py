import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
#Plots all Noisefinder output files
def pdplt():
	dirlist = os.listdir()
	filelist = []
	for file in dirlist:
		if file.endswith(".csv"):
			filelist.append(file)
	for file in filelist:
		mainname = file.replace("_dust_noise.csv","")
		filename = mainname + ".png"
		dt = pd.read_csv(file)
		dt.plot("Pos","Count",markersize=3,color="black",marker="o",linestyle="none",title=mainname)
		plt.ylim([0,(len(filelist))])
		plt.savefig(filename)
"""
#Standalone functionality, future implementation
if len(sys.argv) > 1:
	for i in range(1,len(sys.argv)):
		file = sys.argv[i]
		mainname = file.replace("_dust_noise.csv","")
		filename = mainname + ".png"
		dt = pd.read_csv(file)
		dt.plot("Pos","Count",markersize=3,color="black",marker="o",linestyle="none",title=mainname)
		#plt.ylim([0,(len(filelist))])
		plt.savefig(filename)
else:
	dirlist = os.listdir()
	filelist = []
	for file in dirlist:
		if file.endswith(".csv"):
			filelist.append(file)
	for file in filelist:
		mainname = file.replace("_dust_noise.csv","")
		filename = mainname + ".png"
		dt = pd.read_csv(file)
		dt.plot("Pos","Count",markersize=3,color="black",marker="o",linestyle="none",title=mainname)
		plt.ylim([0,(len(filelist))])
		plt.savefig(filename)
		
"""