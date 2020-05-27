#!/usr/bin/env python

# This script gives you all the RECO data sets that have a corresponding RAW data set, then out of those picks the ones that are CMSSW release 7_0_0 to 10_4_0 && the data sets that are NOT outdated (e.g: data sets that includes teh word 'pre', we found that any jobs submitted for these data sets give us an exit code 8028, which means it couldn't open the data sets.)
	
import sys

f = open("MClist.txt", "w+")
with open("goodfiles.txt" )  as file:
# with open( sys.argv[1]  ) as file:  
	for line in file:
		# deleting the \n character at the end of each line then adding "GEN-SIM-RECO" and going the next line. At this point we only look at the RECO files since our analyzer can get the RAW files from the RECO data sets.
		l = len(line) - 1
		s = line[0:l] 
		f.write(s + "GEN-SIM-RECO\n")
f.close()

f = open("MClist_CMSSW_10_0.txt", "w+")
with open( "MClist.txt" ) as file:
#	if line.find("pre") != -1 :
#		continue
	n = -1 	
    	for line in file:
		# usually before this character you can expect a 3 digit number specifying the CMSSW release. e.g: '102X_' means this data set is compatible with CMSSW 10_2 or later.
    		# n = line.find('X_') # debug1: improvement
		# d1: every dataset has "/CMSSSW_" right before the version (e.g: 9_4_0)
		n = line.find("/CMSSW_")	
		if n != -1 :
			# d1: here we want to get the CMSSW version number, which is from 1 to 16 (? less than 20), currently we want versions from CMSSW_7_0_0 to CMSSW_10_4_0 
			x = line[n+7:n+11] 
			if (x[0] == '9') or (x[0] == '8') or (x[0] == '7'):
				f.write(line)
			if x[0:2] == '10' :
			 	if (x[3] == '0') or (x[3] == '1') or (x[3] == '2') or (x[3] == '3') or (x[3] == '4'):
					f.write(line)
				
f.close()
