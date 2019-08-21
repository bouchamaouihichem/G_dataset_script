#!/bin/sh

# You need a grid certificate to run this script, just google "grid certificate cms cern" to find out how to set it up then use the command 'voms-proxy-init -voms cms' and your type your grid certificate password.

# Get all the GEN-SIM-RECO data sets, then GEN-SIM-DIGI-RAW data sets. 
dasgoclient --query="dataset=/*/*/GEN-SIM-RECO" > GEN-SIM-RECO.txt 
dasgoclient --query="dataset=/*/*/GEN-SIM-DIGI-RAW" > GEN-SIM-DIGI-RAW.txt

# Sort them 
sort GEN-SIM-DIGI-RAW.txt > GEN-SIM-DIGI-RAW_sorted.txt
sort GEN-SIM-RECO.txt > GEN-SIM-RECO_sorted.txt

# This script deletes the last part of the data set "GEN-SIM-RECO" and "GEN-SIM-DIGI-RAW" respectively so that we can compare the 2 output text files in the next step.
python boop.py

# Only take the data sets that are available in both GEN-SIM-RECO and GEN-SIM-DIGI-RAW
comm -1 -2 GEN-SIM-DIGI-RAW_mod.txt GEN-SIM-RECO_mod.txt > goodfiles.txt

# This script gives you all the RECO data sets that have a corresponding RAW data set, then out of those picks the ones that are CMSSW release 10_0_0 or later && the data sets that are NOT outdated (e.g: data sets that includes teh word 'pre', we found that any jobs submitted for these data sets give us an exit code 8028, which means it couldn't open the data sets.)
python oof.py

# This script only includes the data sets that are on Disk (untaped) && the data sets which server the dasgo can locate (no warnings).
python ugh.py

# Remove all the intermediary txt files, you can comment this out for debugging purposes.
rm GEN-SIM-DIGI-RAW*.txt
rm MClist.txt
rm MClist_CMSSW_10_0.txt
rm goodfiles.txt

