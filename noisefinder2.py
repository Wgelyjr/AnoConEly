
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	Noisefinder compares sequences to each other by breaking them into kmers
	and counting the instances of each kmer in all sequences provided.
	
    Copyright (C) 2018  William Ely, Dr. Matthew Jones-Rhoades

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
	
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time
start_time = time.time() #Program execution time
import sys
import re
#Help documentation
if len(sys.argv) <= 1:
	print("Not enough arguments - input -h for help.")
	quit()
	
elif sys.argv[1] == "-h":
	print("Input sequences including their fasta extension, separated by spaces.")
	print("This program will output a .txt file for each file input,")
	print("readable as a table file. This file contains each position of the sequence")
	print("that was input, as well as the count at each position.")
	print("NOTE: This program does not count the number of times a sequence is found,")
	print("but finds the amount of other sequences the target sequence is found in. \n")
	print("Resolution (blocksize) can be changed by the argument <-blocksize n>,")
	print("n being the desired blocksize.")
	quit()

#Method for reading files, courtesy Dr. Matthew Jones-Rhoades (lines 49 to 72)
def read_one_fasta(file):
	# function to read one sequence in FASTA format from a textfile.
	# input: the name (complete path) of the file that contains the sequence to read
	# output: strings containing the Identifier and the Sequence
	# this function will read ONE sequence only.  If more that one sequence is in the file, only first is read

	F = open(file)
	first = 0                        		# will keep track how many ID lines have been found
	ID = ""									# will hold Identifier of sequence
	seq = ""								# will hold Sequence

	for line in F:
		line = line.rstrip("\n")	 		# removes new line characters (returns) from line
		m = re.search(r"^>(\S+)", line)     # uses a Regular Expression to check if line contains ">"
		if m:								# if ID line
			if (first == 0):				# if first ID line
				ID = m.group(1)				# remember ID
				seq = ""					# make sure seq is empty
			first +=1						# remember how many ID lines we have seen
		elif first == 1:
			seq += line						# IF not ID line AND IF if in 1st seqeunce, add line to sequence
	F.close()
	return(ID,seq)

#Change blocksize to adjust signal/noise ratio. Higher blocksize = weaker signal,
#but with a higher significance in found signal. Changed via -blocksize argv.

blocksize = 20

rec = "" #record names
seq2 = "" #The sequence as string
seqdict = {}
countdict = {}
seqkey = {}
filelist = []
fileiter = 0 #protects from out-of-bounds error during name testing

#Need to make each section of output its own file...

print("Parsing files. . .")

for i in range(1,len(sys.argv)):
	targfile = sys.argv[i]
	if targfile == "-blocksize": #Checks targfile for validity as a filename
		blocksize = int(sys.argv[i+1])
		print("Blocksize altered; New value = " + str(blocksize))
		i += 2
	elif sys.argv[i].find(".fasta") != -1: #Second check for filename validity
		filelist.append(sys.argv[i]) #appends actual filenames to filelist list
		(rec,seq2) = read_one_fasta(targfile) #Invokes Matt's function
		seqdict[rec] = seq2 #Stores sequences with recordids as keys
		seqkey[filelist[fileiter]] = rec #ties file names to sequence key for iteration
		fileiter += 1 #Allows the loop to access proper index of filelist

print("Forming kmer dictionaries. . .")

for recordid in seqdict: #Creating kmer:count dictionary
	for i in range(0,len(seqdict[recordid])-blocksize): #Loop for making kmer
		kmer = seqdict[recordid][i:i+blocksize] #Assigns kmer to variable
		countdict[kmer] = 0	#Assigns kmer to key to count - counts matches

print("Forming kmer count dictionaries and counting. . .")

for kmer in countdict: #for every kmer in the count dictionary

	if kmer.find("N") != -1 or kmer.find("n") != -1:
		countdict[kmer] = 0
	elif kmer.find("a") != -1 or kmer.find("c") != -1 or kmer.find("g") != -1 or kmer.find("t") != -1:
		countdict[kmer] = 0
	else:
		for n in range(0, len(filelist)): #For every sequence argument
			string = seqdict[seqkey[filelist[n]]] #String is a sequence from a file
			index = string.find(kmer) #Find the kmer in the string
			if index > -1: countdict[kmer] += 1 #Adding counts to each kmer

print("Writing to files. . .")

for n in range(0, len(filelist)):
	#Constructing files for each sys arg
	name1 = filelist[n]
	name2 = name1.replace(".fasta","")
	name2 = name2 + "_noise.txt"
	f = open(name2,"w+")
	print(">" + filelist[n] + "\n" + "Pos \t Count \t Kmer",file=f)
	string = seqdict[seqkey[filelist[n]]] #String is a sequence from a file
	for pos in range(0,len(string) - (blocksize)): #Loop for making kmer
		kmer = string[pos:pos+blocksize] #Assigns kmer to variable
		print(str(pos) + "\t" + str(countdict[kmer]) + "\t" + kmer,file=f)

minu = " minutes."
hou = " hours."
seco = " seconds."
tottime = (round((time.time() - start_time), 3))
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

print("Complete - Executed in " + str(x) + y)
