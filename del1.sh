#rmdir './FULL_HZZ4l_Bkg_Full'
#rm -r './FULL_HZZ4l_Bkg_Full'
#mv './FULL_HZZ4l_Bkg_Full_1/' './FULL_HZZ4l_Bkg_Full'
path1="/SGE/HEP/toolbox-Mostafa/MG5_aMC_v2_7_3_py3/H400_BLSSM/HWW/Events/"
path2="/HEP_DATA/Mostafa/H400_BLSSM/HWW/"
path1="/SGE/HEP/toolbox-Mostafa/MG5_aMC_v2_7_3_py3/H400_BLSSM/HZZ/Events/"
path2="/HEP_DATA/Mostafa/H400_BLSSM/HZZ/"
path1="/HEP_DATA/Mostafa/H400_BLSSM/Hhhaabb/"
path2="/HEP_DATA/Mostafa/H400_BLSSM/HZZ/"

for i in $(seq 0 200)
do
	for j in $(seq 9 10)
	do
		find $path1'run_0'"$j"'_'"$i"'/' ! -name 'tag_1_delphes_events.root' ! -name 'tag_1_delphes_events.lhco.gz' -type f -exec rm -f {} +
#		mv './FULL_HZZ4l_Bkg_Full/run_07_'"$i"'/' './FULL_HZZ4l_Bkg_Full/run_02_'"$((189+1+$i))"
		echo $j $i
	done
done

for i in $(seq 0 100)
do
	mv $path1'run_xx_'"$i"'/' $path1'run_'"$((186+1+$i))"
#	mv $path1'run_'"$i"'/' './run_'"$(($i-147))"
	echo $i
done

#rmdir ./Events/




for k in $(seq 0 200)
do

	for i in $(seq 0 200)
	do
		for j in $(seq 1 100)
		do
#			find $path1'run_'"$k"'/run_'"$j"'_'"$i"'/' ! -name 'tag_1_delphes_events.root' ! -name 'tag_1_delphes_events.lhco.gz' -type f -exec rm -f {} +
			mv $path1'/run_'"$k"'/run_'"$j"'_'"$i"'/' $path1'/run_xx_'"$((192+1+$k))"
			echo $j $i $k
		done
	done

done


