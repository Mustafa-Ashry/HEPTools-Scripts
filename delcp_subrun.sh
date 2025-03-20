
path1h="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/Hhhaabb_Bkg_Full"
path1z="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/HZZ4l_Bkg_Full"
path1w="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/HWW2lMET_Bkg"

for k in $(seq 1224 1500)
do
	for i in $(seq 0 50)
	do
		for j in $(seq 0 10)
		do
			mv $path1z'/run_'"$k"'/run_0'"$j"'_'"$i"'/' $path1z'/run_'"$((1300+$i))"
#			mv $path1w'/run_'"$k"'/run_0'"$j"'_'"$i"'/' $path1w'/run_'"$((500+$i))"
#			mv $path1h'/run_'"$k"'/run_0'"$j"'_'"$i"'/' $path1h'/run_'"$((500+$i))"
			echo $k $j $i 
		done
	done
done

