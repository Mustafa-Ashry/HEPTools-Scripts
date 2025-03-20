#remove empty dir
#rmdir './HZZ4l_Bkg_Full'
#remove nonempty dir
#rm -r './HZZ4l_Bkg_Full'

#sh ./del_empty.sh
#sh ./rename_order.sh

path1w="/SGE/HEP/toolbox-Mostafa/MG5_aMC_v2_7_3_py3/H400_BLSSM_Bkg/HWW2lMET_Bkg_Full/Events/"
path2w="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/HWW2lMET_Bkg_Full/"
path1z="/SGE/HEP/toolbox-Mostafa/MG5_aMC_v2_7_3_py3/H400_BLSSM_Bkg/HZZ4l_Bkg_Full/Events/"
path2z="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/HZZ4l_Bkg_Full/"
path1h="/SGE/HEP/toolbox-Mostafa/MG5_aMC_v2_7_3_py3/H400_BLSSM_Bkg/Hhhaabb_Bkg_Full/Events/"
path2h="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/Hhhaabb_Bkg_Full/"
wl=$(find /HEP_DATA/Mostafa/H400_BLSSM_Bkg/HWW2lMET_Bkg_Full/* -maxdepth 0 -type d | wc -l)
zl=$(find /HEP_DATA/Mostafa/H400_BLSSM_Bkg/HZZ4l_Bkg_Full/* -maxdepth 0 -type d | wc -l)
hl=$(find /HEP_DATA/Mostafa/H400_BLSSM_Bkg/Hhhaabb_Bkg_Full/* -maxdepth 0 -type d | wc -l)

ni=7
nj=100

for i in $(seq 1 $ni)
do
	for j in $(seq 0 $nj)
	do
		find $path1w'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
		find $path1z'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
		find $path1h'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
	done
done

x=0
for i in $(seq 1 $ni)
do
	for j in $(seq 0 $nj)
	do
		if [ -d $path1w'run_0'"$i"'_'"$j" ]; then
#			find $path1w'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
			x=$(($x+1))
			mv $path1w'run_0'"$i"'_'"$j"'/' $path2w'run_'"$(($wl+$x-1))"
			echo "ww" $i $j $wl $x
		fi
	done
done

y=0
for i in $(seq 1 $ni)
do
	for j in $(seq 0 $nj)
	do
		if [ -d $path1z'run_0'"$i"'_'"$j" ]; then
#			find $path1z'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
			y=$(($y+1))
			mv $path1z'run_0'"$i"'_'"$j"'/' $path2z'run_'"$(($zl+$y-1))"
			echo "zz" $i $j $zl $y
		fi
	done
done

z=0
for i in $(seq 1 $ni)
do
	for j in $(seq 0 $nj)
	do
		if [ -d $path1h'run_0'"$i"'_'"$j" ]; then
#			find $path1h'run_0'"$i"'_'"$j"'/' ! -name '*.root' ! -name '*.lhco.gz' -type f -exec rm -f {} +
			z=$(($z+1))
			mv $path1h'run_0'"$i"'_'"$j"'/' $path2h'run_'"$(($hl+$z-1))"
			echo "hh" $i $j $hl $z
		fi
	done
done






