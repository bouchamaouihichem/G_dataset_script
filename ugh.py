#!/usr/bin/env python

# This script only includes the data sets that are on Disk (untaped) && the data sets which server the dasgo can locate (no warnings).
		
import sys
import os
import subprocess

f = open("MClist_CMSSW_10_0_untaped.txt", "w+")
with open ( "MClist_CMSSW_10_0.txt" ) as file:
	n = -1
	for line in file:
		str ='dasgoclient --query="site dataset='+ line[:-1] + '"'
		result = subprocess.check_output(str,shell=True)
		# result = terminal output basically
		if result.find("Disk") != -1 and result.find("WARNING") == -1:
			f.write(line)
f.close()

