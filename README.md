# AnoConEly
Analysis of Conservation within Insect Dscam Genes

___

Preface from several years later...

I've learned a lot of Python since this first real project. I also took this project and its 'documentation' very seriously, as that's what I was encouraged to do by my professors. Keep that in mind as you read!

___

DSCAM research by Liam Ely
Contact at Wgely(at)knox.edu

Sequence data retrieved from NCBI, found with NCBI's BLASTN/BLAST+
Editing source code done in Notepad++

The paper that inspired this research: 
https://www.sciencedirect.com/science/article/pii/S0092867405007592?via%3Dihub

A very special thank you to Dr. Matthew Jones-Rhoades and Dr. Ole Foresberg.

The program used to construct these data from the sequences is the Noisefinder
program. You'll find documentation for the program within the source code or
by running the program with the argument <-h>...

The gist is you go to your directory that contains the .fasta files you want to
analyze in cmd. Then, for example:

Noisefinder2.py testgene.fasta testgene2.fasta testgene3.fasta

In the same directory, the files containing the data (one for each analyzed file)
will be generated.

There are two versions of Noisefinder - 2 and 3. 2 is far more lightweight, and 
only spits out tables of data in the directory it was pathed to, while 3 has
a bunch of modules tacked onto it that plot the tables and organize the resulting
pngs and csvs into their own folders. Get familiar with 2 before you experiment 
with 3, especially if you're just here to dissect the source code. :)

The .fasta files included here are the DSCAM genes of a number of insects. They have
a number of regions that are highly conserved; the purpose of said regions will become
very clear after reading the paper by Dr. Brenton Graveley, linked above.

All of these files and data are yours to manipulate, but hopefully you'll help me
perfect this script and let me know about anything interesting you find!

Feel free to email me any questions, concerns, or comments!
