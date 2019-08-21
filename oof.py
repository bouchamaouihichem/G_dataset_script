#!/usr/bin/env python

# This script gives you all the RECO data sets that have a corresponding RAW data set, then out of those picks the ones that are CMSSW release 10_0_0 or later && the data sets that are NOT outdated (e.g: data sets that includes teh word 'pre', we found that any jobs submitted for these data sets give us an exit code 8028, which means it couldn't open the data sets.)
		
import sys

f = open("MClist.txt", "w+")
with open("goodfiles.txt" )  as file:
# with open( sys.argv[1]  ) as file:  
	for line in file:
		# deleting the \n character at the end of each line then adding "GEN-SIM-RECO" and going the next line. At this point we only look at the RECO files since our analyzer can get the RAW files from teh RECO data sets.
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
    		n = line.find('X_')
		# usually before this character you can expect a 3 digit number specifying the CMSSW release. e.g: '102X_' means this data set is compatible with CMSSW 10_2 or later.
		if n != -1 :
			# This trick only works because I'm looking at CMSSW 10_0_0 or later releases, if you need a different version then you need to edit this part.
			x = line[n-3] # 
			if x == '1' :
				f.write(line)
f.close()
