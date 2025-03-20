#remove empty dir
#rmdir './HZZ4l'
#remove nonempty dir
#rm -r './HZZ4l'

#sh ./del_empty.sh
#sh ./rename_order.sh

path1w="/SGE/HEP/toolbox-Mostafa/MG5_aMC_v2_7_3_py3/H400_BLSSM/HWW/Events/"
path2w="/HEP_DATA/Mostafa/H400_BLSSM/HWW/"
path1z="/SGE/HEP/toolbox-Mostafa/MG5_aMC_v2_7_3_py3/H400_BLSSM/HZZ/Events/"
path2z="/HEP_DATA/Mostafa/H400_BLSSM/HZZ/"
path1h="/SGE/HEP/toolbox-Mostafa/MG5_aMC_v2_7_3_py3/H400_BLSSM/Hhhaabb/Events/"
path2h="/HEP_DATA/Mostafa/H400_BLSSM/Hhhaabb/"
wl=$(find /HEP_DATA/Mostafa/H400_BLSSM/HWW/* -maxdepth 0 -type d | wc -l)
zl=$(find /HEP_DATA/Mostafa/H400_BLSSM/HZZ/* -maxdepth 0 -type d | wc -l)
hl=$(find /HEP_DATA/Mostafa/H400_BLSSM/Hhhaabb/* -maxdepth 0 -type d | wc -l)

ni1=2
ni2=2
nj1=33
nj2=36

for i in $(seq $ni1 $ni2)
do
	for j in $(seq $nj1 $nj2)
	do
		find $path1w'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
		find $path1z'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
		find $path1h'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
	done
done

x=0
for i in $(seq $ni1 $ni2)
do
	for j in $(seq $nj1 $nj2)
	do
		if [ -d $path1w'run_0'"$i"'_'"$j" ]; then
#			find $path1w'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
			x=$(($x+1))
			mv $path1w'run_0'"$i"'_'"$j"'/' $path2w'run_'"$(($wl+$x-1))"
			echo "ww" $i $j $wl $(($wl+$x-1))
		fi
	done
done

y=0
for i in $(seq $ni1 $ni2)
do
	for j in $(seq $nj1 $nj2)
	do
		if [ -d $path1z'run_0'"$i"'_'"$j" ]; then
#			find $path1z'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
			y=$(($y+1))
			mv $path1z'run_0'"$i"'_'"$j"'/' $path2z'run_'"$(($zl+$y-1))"
			echo "zz" $i $j $zl $(($zl+$y-1))
		fi
	done
done

z=0
for i in $(seq $ni1 $ni2)
do
	for j in $(seq $nj1 $nj2)
	do
		if [ -d $path1h'run_0'"$i"'_'"$j" ]; then
#			find $path1h'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
			z=$(($z+1))
			mv $path1h'run_0'"$i"'_'"$j"'/' $path2h'run_'"$(($hl+$z-1))"
			echo "hh" $i $j $hl $(($hl+$z-1))
		fi
	done
done






