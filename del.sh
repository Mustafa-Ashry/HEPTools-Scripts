for i in $(seq 0 200)
do
	find ./ppww2lmet_bkg_$i -mindepth 1 ! -regex '^./ppww2lmet_bkg_'"$i"'/Events\(/.*\)?' -delete
	echo $i
done

for i in $(seq 0 200)
do
	mv './ppww2lmet_bkg_'"$i"'/Events/run_01' './run_'"$i"
	rmdir './ppww2lmet_bkg_'"$i"
	rm -r './ppww2lmet_bkg_'"$i"
	echo $i
done






for i in $(seq 0 200)
do
	find './run_'"$i"'/' ! -name 'tag_1_delphes_events.root' ! -name 'tag_1_delphes_events.lhco.gz' -type f -exec rm -f {} +
	echo $i
done
