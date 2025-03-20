
path1w="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/HWW2lMET_Bkg_Full"
path1z="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/HZZ4l_Bkg_Full"
path1h="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/Hhhaabb_Bkg_Full"

for k in $(seq 0 1000)
do
	rmdir $path1w'/run_'"$k"'/'
	rmdir $path1z'/run_'"$k"'/'
	rmdir $path1h'/run_'"$k"'/'
	echo $k
done

