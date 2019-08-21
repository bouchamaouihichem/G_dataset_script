#!/usr/bin/env python

# This script deletes the last part of the data set "GEN-SIM-RECO" and "GEN-SIM-DIGI-RAW" respectively so that we can compare the 2 output text files in the next step.

import sys

f= open("GEN-SIM-RECO_mod.txt","w+")
with open("GEN-SIM-RECO_sorted.txt" )  as file:
	for line in file:
    		n = line.find("GEN-SIM-RECO")
		if n != -1 : 
	   		f.write(line[0:n] + '\n')
f.close()

g= open("GEN-SIM-DIGI-RAW_mod.txt","w+")
with open("GEN-SIM-DIGI-RAW_sorted.txt" ) as file:
	for line in file:
 		n = line.find("GEN-SIM-DIGI-RAW")
		if n != -1 :
			g.write(line[0:n] + '\n')
g.close()

