#Module that reads .fasta files, returns ID and sequence

import re
def read_fasta(file):
	# written by Dr. Matthew Jones-Rhoades
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