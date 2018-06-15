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
		name = file.replace("_dust_noise.csv","")
		name = name + ".png"
		dt = pd.read_csv(file)
		dt.plot("Pos","Count",markersize=3,color="black",marker="o",linestyle="none")
		plt.ylim([0,(len(filelist))])
		plt.savefig(name)
