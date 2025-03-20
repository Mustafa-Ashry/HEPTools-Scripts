###############################################################
## This file code was created by Mustafa Ashry in March 2020 ##
###############################################################
#!/bin/sh
#Run: chmod +x script_1_split.txt#Then: run ./script_1_split.txt
# or only run: 
#sh -e script_1_split.txt
#sh ./script_1_split.sh
for i in $(seq 0 150)
do
	if [ -e "/home/mashry/hep/SSP-1.2.5/Output/BLSSMScanLowmh$i/SpectrumFiles.spc" ]
#		csplit --suppress-matched -z -n 1 -f /home/mashry/hep/SSP-1.2.5/Output/BLSSMScanLowmh$i/SPheno.spc.BLSSM_$i"_" /home/mashry/hep/SSP-1.2.5/Output/BLSSMScanLowmh$i/SpectrumFiles.spc /ENDOFPARAMETERFILE/  '{*}'
	then
		csplit --suppress-matched -z -n 1 -f /home/mashry/hep/SSP-1.2.5/Output/BLSSMScanLowmh/SPheno.spc.BLSSM_$i"_" /home/mashry/hep/SSP-1.2.5/Output/BLSSMScanLowmh$i/SpectrumFiles.spc /ENDOFPARAMETERFILE/  '{*}'
	fi
done
