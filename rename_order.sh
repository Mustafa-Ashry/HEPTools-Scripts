
path1w="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/HWW2lMET_Bkg_Full"
path1z="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/HZZ4l_Bkg_Full"
path1h="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/Hhhaabb_Bkg_Full"

x=0
for k in $(seq 0 1000)
do
	if [ -d $path1w'/run_'"$k" ]; then
		x=$(($x+1))
		mv $path1w'/run_'"$k"'/' $path1w'/run_'"$(($x-1))"
		echo $k $x
	fi
done

y=0
for k in $(seq 0 1500)
do
	if [ -d $path1z'/run_'"$k" ]; then
		y=$(($y+1))
		mv $path1z'/run_'"$k"'/' $path1z'/run_'"$(($y-1))"
		echo $k $y
	fi
done

z=0
for k in $(seq 0 1500)
do
	if [ -d $path1h'/run_'"$k" ]; then
		z=$(($z+1))
		mv $path1h'/run_'"$k"'/' $path1h'/run_'"$(($z-1))"
		echo $k $z
	fi
done

